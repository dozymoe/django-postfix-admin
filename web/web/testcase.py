"""Prepare test client
"""
from django.conf import settings
from django.contrib.sites.models import Site
from django.test import TestCase
#-
from my_user.models import User

class BaseTestCase(TestCase):
    """Prepare model instances and configuration
    """
    @classmethod
    def setUpTestData(cls):
        """Prepare testing models
        """
        # Create Site
        cls.server_name = settings.ALLOWED_HOSTS[0]
        cls.site = Site.objects.create(domain=cls.server_name,
                name="Testing Site")
        cls.user = User.objects.create_user(username='user', password='12345')


    def loginUser(self):
        """Prepare login session
        """
        login = self.client.login(username='user', password='12345')
        self.assertTrue(login)
