from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page(self):
        '''Test root url resolve to home page'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        '''Test home page return write html'''
        request = HttpRequest()
        response = home_page(request)
        html = response.content
        self.assertTrue(html.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith(b'</html>'))



