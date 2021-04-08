"""Helpjuice Users API.

https://help.helpjuice.com/en_US/api-v3/api-v3#users
"""
from helpjuice.api.schema import Collection
from helpjuice.api.schema import Resource


class User(Resource):
    """User

    https://help.helpjuice.com/en_US/api-v3/api-v3#users

    Attributes:
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
        email (str): Unique email of the user.
        role_id (str): Role of the user.
        group_ids (list): Ids of the groups where the user should be joined.
    """

    def get(self):
        """Retrieve a user.

        https://help.helpjuice.com/en_US/api-v3/api-v3#retrieve-a-user

        Returns:
            :obj:`helpjuice.api.User`: Requested user.
        """
        return super().get("users")

    def post(self):
        """Create a New user.

        https://help.helpjuice.com/en_US/api-v3/api-v3#create-a-new-user

        Returns:
            :obj:`helpjuice.api.User`: Requested user.
        """
        return super().post("users")

    def put(self):
        """Update a user.

        https://help.helpjuice.com/en_US/api-v3/api-v3#retrieve-a-user

        Returns:
            :obj:`helpjuice.api.User`: Requested user.
        """
        return super().put("users")

    def delete(self):
        """Retrieve a user.

        https://help.helpjuice.com/en_US/api-v3/api-v3#retrieve-a-user

        Returns:
            :obj:`helpjuice.api.User`: Requested user.
        """
        return super().delete("users")


class Users(Collection):
    """User collection.

    https://help.helpjuice.com/en_US/api-v3/api-v3#users
    """

    resource = User

    def get(self, *args, **kwargs):
        """Retrieve all users.

        https://help.helpjuice.com/en_US/api-v3/api-v3#retrieve-all-users

        Returns:
            :obj:`helpjuice.api.Users`: Requested users.
        """
        return super().get("users", *args, **kwargs)
