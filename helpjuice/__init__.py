"""Helpjuice API wrapper

https://help.helpjuice.com/en_US/api-v3/api-v3

Overview
========
Version 3 of the Helpjuice API is structured around REST, HTTP, and JSON. API endpoint
URLs are organized around resources, such as users or articles. It uses HTTP methods for
indicating the action to take on a resource, and HTTP status codes for expressing error
statues. Resources are represented in JSON following a conventional schema.
"""
from helpjuice.__version__ import __author__
from helpjuice.__version__ import __author_email__
from helpjuice.__version__ import __copyright__
from helpjuice.__version__ import __description__
from helpjuice.__version__ import __license__
from helpjuice.__version__ import __title__
from helpjuice.__version__ import __url__
from helpjuice.__version__ import __version__
from helpjuice.client import Client

__all__ = ["Client"]
