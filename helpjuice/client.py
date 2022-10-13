"""Client

This module provides a Client object to interface with the Helpjuice API.
"""
import logging

from requests import HTTPError
from requests import Session
from requests.adapters import HTTPAdapter
from requests.auth import HTTPBasicAuth
from requests.compat import urljoin
from requests.packages.urllib3.util.retry import Retry  # type: ignore

from helpjuice.api import *
from helpjuice.errors import UnprocessableEntity

try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version

logger = logging.getLogger(__name__)
__version__ = version("helpjuice")


class HelpjuiceAuth(HTTPBasicAuth):
    """Attaches API Key Authentication to the given Request object."""

    def __init__(self, api_key):
        self.api_key = api_key

    def __eq__(self, other):
        return self.api_key == getattr(other, "api_key", None)

    def __call__(self, r):
        logger.info(f"{r.method} {r.url}")
        r.headers["Authorization"] = self.api_key
        return r


class Client(Session):
    """Helpjuice Client.

    Constructs a :obj:`requests.Session` for Helpjuice API requests with
    authorization, base URL, request timeouts, and request retries.

    Args:
        account (str): Helpjuice base address subdomain.
        api_key (str): Helpjuice API key.
        version (str, optional): Helpjuice API version. Defaults to "v3".
        timeout (int, optional): :obj:`TimeoutHTTPAdapter` timeout value. Defaults to 5.
        total (int, optional): :obj:`Retry` total value. Defaults to 5.
        backoff_factor (int, optional): :obj:`Retry` backoff_factor value.
            Defaults to 30.

    Usage::

      from helpjuice import Client

      helpjuice = Client(account="your-account", api_key="ffb722a62e8**********************")

      # Get a single article
      article = helpjuice.Article(id=1).get()

      # Search for articles with pagination
      for question in helpjuice.Search().get(query="foo", limit=1000, paginate=True):
          print(question)
    """

    def __init__(self, account, api_key, v="v3", timeout=5, total=5, backoff_factor=30):
        """Helpjuice Client constructor.

        Constructs a :obj:`requests.Session` for Helpjuice API requests with
        authorization, base URL, request timeouts, and request retries.

        Args:
            account (str): Helpjuice base address subdomain.
            api_key (str): Helpjuice API key.
            version (str, optional): Helpjuice API version. Defaults to "v3".
            timeout (int, optional): :obj:`TimeoutHTTPAdapter` timeout value. Defaults to 5.
            total (int, optional): :obj:`Retry` total value. Defaults to 5.
            backoff_factor (int, optional): :obj:`Retry` backoff_factor value.
                Defaults to 30.
        """
        super().__init__()

        self.auth = HelpjuiceAuth(api_key=api_key)
        self.host = f"https://{account}.helpjuice.com/api/{v}/"
        self.headers.update({"User-Agent": f"python-helpjuice/{__version__}"})

        adapter = TimeoutHTTPAdapter(
            timeout=timeout,
            max_retries=Retry(
                total=total,
                status_forcelist=[429, 500, 502, 503, 504],
                backoff_factor=backoff_factor,
            ),
        )
        self.mount("https://", adapter)
        self.mount("http://", adapter)

        self.__build_resources()

    def __build_resources(self):
        """Add each resource with a reference to this instance."""
        for k, v in globals().items():
            try:
                for base in v.__bases__:
                    if base.__name__ not in ["Collection", "Resource"]:
                        continue

                    v._client = self
                    setattr(self, k, v)

            except AttributeError:
                continue

    def request(self, method, path, *args, **kwargs):
        """Override :obj:`Session` request method to add retries and output JSON.

        Args:
            method (str): Method for the new Request object.
            path (str): Path from host for the new Request object.

        Returns:
            dict: Response JSON
        """
        if not isinstance(path, str):
            path = "/".join((str(s) for s in path if s))
        path = path.rstrip("/")

        response = super().request(
            method=method, url=urljoin(self.host, path), *args, **kwargs
        )
        try:
            response.raise_for_status()
        except HTTPError as exc:
            code = exc.response.status_code

            if code == 422:
                raise UnprocessableEntity(exc.request, exc.response) from exc
            else:
                raise

        json = response.json()
        meta = json.pop("meta", None)
        resource, *_ = json.values()

        if meta:
            return resource, meta
        return resource


class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, timeout, *args, **kwargs):
        """TimeoutHTTPAdapter constructor.

        Args:
            timeout (int): How many seconds to wait for the server to send data before
                giving up.
        """
        self.timeout = timeout
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        """Override :obj:`HTTPAdapter` send method to add a default timeout."""
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout

        return super().send(request, **kwargs)
