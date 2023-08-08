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
        response = self.client.get('/')

        html = response.content

        self.assertTrue(html.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith(b'</html>'))

        self.assertTemplateUsed(response, "home.html")
 
    def test_can_save_a_POST_request(self):
        '''Can save post request test'''
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn(b'A new list item', response.content)
        self.assertTemplateUsed(response, 'home.html')