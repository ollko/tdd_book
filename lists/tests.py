from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page
from lists.models import Item

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
        self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.all().count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
    
    def test_redirect_after_POST(self):
        '''Redirect after POST test'''
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')      
    
    def test_only_saves_items_when_necessary(self):
        '''Only save items when necessary'''
        self.client.get('/')
        self.assertEqual(Item.objects.all().count(), 0)
    
    def test_displays_all_list_items (self):
        '''Rendering all items oon the page test'''
        Item.objects.create(text='itemy 1')
        Item.objects.create(text='itemy 2')

        response = self.client.get('/')

        self.assertIn(b'itemy 1', response.content)
        self.assertIn(b'itemy 2', response.content)



class ItemModelTest(TestCase):
    '''List item test'''

    def test_saving_and_retrieving_items(self):
        '''Saving and retrieving test'''
        first_item = Item()
        first_item.text = 'The first list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'The second list item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first list item')
        self.assertEqual(second_saved_item.text, 'The second list item')
