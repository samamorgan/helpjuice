"""Helpjuice Categories API.

https://help.helpjuice.com/en_US/api-v3/api-v3#categories
"""
from helpjuice.api.schema import Collection
from helpjuice.api.schema import Resource


class Category(Resource):
    """Category resource.

    Attributes:
        parent_id (int): The ID of the parent category.
        accessibility (int): (public: 0, internal: 1, private: 2) Limited the access to
            articles inside.
        description (str): Description of the category.
        name (str): Name of the category.
        codename (str): The slug for the category.
        archived (bool): Whether the category is archived or not.
        user_ids (list): If accessibility is set to private, these users will have
            access to it.
        group_ids (list): If accessibility is set to private, these group members will
            have access to it.
    """

    def get(self):
        """Retrieve an category.

        https://help.helpjuice.com/en_US/api-v3/api-v3#retrieve-an-category

        Returns:
            :obj:`helpjuice.api.Category`
        """
        return super().get("categories")

    def post(self):
        """Create an category.

        https://help.helpjuice.com/en_US/api-v3/api-v3#create-an-category

        Returns:
            :obj:`helpjuice.api.Category`
        """
        return super().post("categories")

    def put(self):
        """Update an category.

        https://help.helpjuice.com/en_US/api-v3/api-v3#update-an-category

        Returns:
            :obj:`helpjuice.api.Category`
        """
        return super().put("categories")

    def delete(self):
        """Delete an category.

        https://help.helpjuice.com/en_US/api-v3/api-v3#delete-an-category
        """
        return super().delete("categories")


class Categories(Collection):
    """Category resource collection."""

    resource = Category

    def get(self, *args, **kwargs):
        """Retrieve all categories.

        https://help.helpjuice.com/en_US/api-v3/api-v3#retrieve-all-categories

        Returns:
            :obj:`helpjuice.api.Categories`
        """
        return super().get("categories", *args, **kwargs)
