"""Helpjuice Search API.

https://help.helpjuice.com/en_US/api-v3/api-v3#search
"""
from helpjuice.api.article import Article
from helpjuice.api.schema import Collection


class SearchResult(Article):
    """Search result resource.

    Attributes:
        id (int): Identifier of the article.
        name (str): Name of the article.
        slug (str): URL slug of the article.
        tag_names (list): Tag names of the article.
        answer_sample (str): Short answer of the article in a few words.
        long_answer_sample (str): Longer answer of the article but not a full article.
        categories (dict): Categories that the article will appear in.
        last_published_date (str): Last published date of the article.
        last_published_user_name (str): Last publisher of the article.
        is_published (bool): Whether the article is published or not.
        is_internal (bool): Whether the article is internal or not.
        url (str): Url of the article.
    """

    pass


class Search(Collection):
    """Search result resource collection.

    https://help.helpjuice.com/en_US/api-v3/api-v3#search
    """

    resource = SearchResult

    def get(self, query, *args, **kwargs):
        """Search the Knowledge Base.

        https://help.helpjuice.com/en_US/api-v3/api-v3#search-the-knowledge-base

        Args:
            query (str): Search query.

        Returns:
            :obj:`helpjuice.api.Search`: Search results.
        """
        return super().get("search", params={"query": query}, *args, **kwargs)
