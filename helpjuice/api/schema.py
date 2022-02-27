"""Schema

https://help.helpjuice.com/en_US/api-v3/api-v3#schema

All API requests and response bodies adhere to a common JSON format representing
individual items and collections of items.
"""


class SchemaBase:
    _client = None


class Resource(dict, SchemaBase):
    """Single Resource.

    https://help.helpjuice.com/en_US/api-v3/api-v3#single-resources

    Individual resources are represented by top level member named after the resource in
    the singular form. Below is a representation of a single contact. This could be used
    in the body of a PUT request and it’s what would be returned in the body of a GET
    request.
    """

    def __getattr__(self, name):
        try:
            return super().__getitem__(name)
        except KeyError:
            try:
                return super().__getattribute__(name)
            except AttributeError as e:
                raise AttributeError(e) from None

    def __setattr__(self, name, value):
        super().__setitem__(name, value)

    def __str__(self):
        id = getattr(self, "id", "")

        return f"{self.__class__.__name__} #{id}" if id else self.__class__.__name__

    def __repr__(self):
        return object.__repr__(self)

    def get(self, resource, subresource=None, *args, **kwargs):
        """Retrieve a resource.

        https://help.helpjuice.com/en_US/api-v3/api-v3#http-methods

        Args:
            resource (str): Resource endpoint.

        Returns:
            :obj:`helpjuice.Resource`: Requested resource.
        """
        response = self._client.get(
            [resource, subresource, getattr(self, "id", None)], *args, **kwargs
        )
        self.update(response)

        return self

    def post(self, resource, *args, **kwargs):
        """Create a new resource.

        https://help.helpjuice.com/en_US/api-v3/api-v3#http-methods

        Args:
            resource (str): Resource endpoint.

        Returns:
            :obj:`helpjuice.Resource`: Created resource.
        """
        response = self._client.post(
            resource,
            json={self.__class__.__name__.lower(): self},
            *args,
            **kwargs,
        )
        self.update(response)

        return self

    def put(self, resource, *args, **kwargs):
        """Update a resource.

        https://help.helpjuice.com/en_US/api-v3/api-v3#http-methods

        Args:
            resource (str): Resource endpoint.

        Returns:
            :obj:`helpjuice.api.Resource`: Updated resource.
        """
        response = self._client.put(
            [resource, getattr(self, "id", None)],
            json={self.__class__.__name__.lower(): self},
            *args,
            **kwargs,
        )

        self.update(response)

        return self

    def delete(self, resource, *args, **kwargs):
        """Remove a resource.

        https://help.helpjuice.com/en_US/api-v3/api-v3#http-methods

        Args:
            resource (str): Resource endpoint.
        """
        response = self._client.delete(
            [resource, getattr(self, "id", None)], *args, **kwargs
        )
        self.update(response)

        return self


class Collection(list, SchemaBase):
    """Resource Collection.

    https://help.helpjuice.com/en_US/api-v3/api-v3#collections

    Collections of resources are represented by a top level member named after the
    resource in the plural form.
    """

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.__class__(*super().__getitem__(index))

        return super().__getitem__(index)

    def __repr__(self):
        return object.__repr__(self)

    def get(self, resource, paginate=False, *args, **kwargs):
        """Retrieve a collection of resources.

        https://help.helpjuice.com/en_US/api-v3/api-v3#http-methods

        Args:
            resource (str): Resource endpoint.
            paginate (bool, optional): Whether to paginate results. Defaults to False.

        Returns:
            :obj:`helpjuice.Collection`: Requested resources.
        """
        paginator = PageIterator(self, resource, *args, **kwargs)

        if paginate:
            return paginator

        self.clear()
        for n, _ in enumerate(paginator):
            if n == paginator.limit - 1:
                break

        return self


class PageIterator:
    """Page Iterator.

    https://help.helpjuice.com/en_US/api-v3/api-v3#pagination

    Attributes:
        collection (:obj:`helpjuice.Collection`): Resource collection to append
                results to.
        resource (str): Resource endpoint.
        limit (int, optional): The number of results to display in each page.
    """

    def __init__(self, collection, resource, limit=25, *args, **kwargs):
        """Page Iterator constructor.

        Endpoints that return collections of resources must limit the number of records
        returned in a given response. A typical endpoint will return 25 records by
        default, the query parameter `limit` can be used to alter the number of records
        returned.

        Args:
            collection (:obj:`helpjuice.Collection`): Resource collection to append
                results to.
            resource (str): Resource endpoint.
            limit (int, optional): The number of results to display in each page.
                Defaults to 25, max 1000.
        """
        self.collection = collection
        self.resource = resource
        self.limit = limit

        if limit != 25:
            kwargs.setdefault("params", {}).update(limit=limit)

        self.args = args
        self.kwargs = kwargs

    def __iter__(self):
        self.page = 1
        self.total_pages = 1
        self._resources = []

        return self

    def __next__(self):
        if self.resources:
            return self.resources.pop(0)

        if self.page <= self.total_pages:
            self.kwargs.setdefault("params", {}).update(page=self.page)
            self.resources, meta = self.collection._client.get(
                self.resource, *self.args, **self.kwargs
            )
            self.total_pages = meta["total_pages"]
            self.page = meta["current"] + 1

            return next(self)

        raise StopIteration

    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, value):
        self._resources = [self.collection.resource(v) for v in value]
        self.collection.extend(self.resources)
