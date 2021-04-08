"""Helpjuice Settings API.

https://help.helpjuice.com/en_US/api-v3/api-v3#settings
"""

from helpjuice.api.schema import Resource


class Settings(Resource):
    """Settings resource.

    Attributes:
        name (str): Name of your account.
        subdomain (str): Name of your account in snake_case.
        top_questions_count (int): The number of articles that will be shown in your kb.
        internal_kb (bool): Use your kb internally only.
        expire_password_after_days (int): Password expiration for new users, number of
            days.
        contact_us_email (str): Support Email address.
        contact_us_subject (str): Contact us emails, subject line.
        contact_us_single_sender (bool): Send all contact us emails asset in
            `contact_us_email` field.
        only_internal_article_requests (bool): Character encoding for requests and reports.
        created_at (str): Account creation timestamp.
    """

    def get(self):
        """Retrieve account settings.

        https://help.helpjuice.com/en_US/api-v3/api-v3#retrieve-account-settings

        Returns:
            :obj:`helpjuice.api.Settings`: Account settings.
        """
        return super().get("settings", "account")

    def put(self):
        """Update account settings.

        https://help.helpjuice.com/en_US/api-v3/api-v3#update-account-settings

        Returns:
            :obj:`helpjuice.api.Settings`: Account settings.
        """
        return super().put("settings")
