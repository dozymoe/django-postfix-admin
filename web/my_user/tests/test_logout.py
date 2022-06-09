"""Test the account logout page
"""
from urllib.parse import urlencode
#-
from web.testcase import BaseTestCase

class LogoutPage(BaseTestCase):
    """Test index page
    """
    def test_get(self):
        """GET request as anon user
        """
        self.loginUser()
        response = self.client.get('/account/logout/',
                SERVER_NAME=self.server_name)
        self.assertEqual(response.status_code, 302)


    def test_get_anon(self):
        """GET request as anon user
        """
        response = self.client.get('/account/logout/',
                SERVER_NAME=self.server_name)
        self.assertEqual(response.status_code, 302)
