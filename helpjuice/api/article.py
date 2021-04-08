"""Helpjuice Articles API.

https://help.helpjuice.com/en_US/api-v3/api-v3#articles
"""
from helpjuice.api.schema import Collection
from helpjuice.api.schema import Resource


class Article(Resource):
    """Article resource.

    Attributes:
        id (int): Identifier of the article.
        name (str): Name of the article.
        description (str): Description of the article.
        codename (str): Slug or URL for the article.
        visibility_id (int): (public: 0, internal: 1, private: 2) Limited access to the
            article.
        body (str): Body of the article.
        published (bool): Whether the article is published or not.
        category_ids (list): Categories that the article will appear in.
        user_ids (list): If accessibility is set to private, these users will have
            access to it.
        group_ids (list): If accessibility is set to private, these group members will
            have access to it.
        contributor_user_ids (list): Article contributors.
    """

    def get(self):
        """Retrieve an article.

        https://help.helpjuice.com/en_US/api-v3/api-v3#retrieve-an-article

        Returns:
            :obj:`helpjuice.api.Article`
        """
        return super().get("articles")

    def post(self):
        """Create an article.

        https://help.helpjuice.com/en_US/api-v3/api-v3#create-an-article

        Returns:
            :obj:`helpjuice.api.Article`
        """
        return super().post("articles")

    def put(self):
        """Update an article.

        https://help.helpjuice.com/en_US/api-v3/api-v3#update-an-article

        Returns:
            :obj:`helpjuice.api.Article`
        """
        return super().put("articles")

    def delete(self):
        """Delete an article.

        https://help.helpjuice.com/en_US/api-v3/api-v3#delete-an-article
        """
        return super().delete("articles")


class Articles(Collection):
    """Article resource collection."""

    resource = Article

    def get(self, *args, **kwargs):
        """Retrieve all articles.

        https://help.helpjuice.com/en_US/api-v3/api-v3#retrieve-all-articles

        Returns:
            :obj:`helpjuice.api.Articles`
        """
        return super().get("articles", *args, **kwargs)
