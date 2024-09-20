# main/tests/test_urls.py
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import home, logout

class UrlsTest(SimpleTestCase):

    def test_home_url_resolves(self):
        """Test that the home URL resolves to the home view"""
        url = reverse('main:home')
        self.assertEqual(resolve(url).func, home)

    def test_logout_url_resolves(self):
        """Test that the logout URL resolves to the logout view"""
        url = reverse('main:logout')
        self.assertEqual(resolve(url).func, logout)

    def test_home_url_reverse(self):
        """Test reverse URL for home"""
        url = reverse('main:home')
        self.assertEqual(url, '/')

    def test_logout_url_reverse(self):
        """Test reverse URL for logout"""
        url = reverse('main:logout')
        self.assertEqual(url, '/logout/')
