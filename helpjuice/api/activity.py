"""Helpjuice Activities API.

https://help.helpjuice.com/en_US/api-v3/api-v3#settings
"""
from helpjuice.api.schema import Collection
from helpjuice.api.schema import Resource


class Activity(Resource):
    """Activity resource.

    Attributes:
        id (int): Activity ID.
        trackable_id (int): Trackable resource ID.
        trackable_type (int): Trackable resource type.
        owner_id (int): Activity user ID.
        action (int): Activity performed.
        created_at (int): Timestamp activity was performed.
    """

    def get(self):
        """Retrieve an activity.

        https://help.helpjuice.com/en_US/api-v3/api-v3#retrieve-an-activity

        Returns:
            :obj:`helpjuice.api.Activity`
        """
        return super().get("activities")


class Activities(Collection):
    """Activity resource collection."""

    resource = Activity

    def get(self, *args, **kwargs):
        """Retrieve all activities.

        https://help.helpjuice.com/en_US/api-v3/api-v3#retrieve-all-activities

        Returns:
            :obj:`helpjuice.api.Activities`
        """
        return super().get("activities", *args, **kwargs)
