"""Helpjuice Groups API.

https://help.helpjuice.com/en_US/api-v3/api-v3#groups
"""
from helpjuice.api.schema import Collection
from helpjuice.api.schema import Resource


class Group(Resource):
    """Group resource.

    Attributes:
        name (str): Name of the group.
        smart_load (bool): Enable smart loading users in this group.
        user_ids (list): Join users to this group.
        auto_groups (str): A comma-separated string of email extension that will be
            auto-loaded to this group. `smart_load` has to be enabled.
    """

    def get(self):
        """Retrieve an group.

        https://help.helpjuice.com/en_US/api-v3/api-v3#retrieve-an-group

        Returns:
            :obj:`helpjuice.api.Group`
        """
        return super().get("groups")

    def post(self):
        """Create an group.

        https://help.helpjuice.com/en_US/api-v3/api-v3#create-an-group

        Returns:
            :obj:`helpjuice.api.Group`
        """
        return super().post("groups")

    def put(self):
        """Update an group.

        https://help.helpjuice.com/en_US/api-v3/api-v3#update-an-group

        Returns:
            :obj:`helpjuice.api.Group`
        """
        return super().put("groups")

    def delete(self):
        """Delete an group.

        https://help.helpjuice.com/en_US/api-v3/api-v3#delete-an-group
        """
        return super().delete("groups")


class Groups(Collection):
    """Group resource collection."""

    resource = Group

    def get(self, *args, **kwargs):
        """Retrieve all groups.

        https://help.helpjuice.com/en_US/api-v3/api-v3#retrieve-all-groups

        Returns:
            :obj:`helpjuice.api.Groups`
        """
        return super().get("groups", *args, **kwargs)
