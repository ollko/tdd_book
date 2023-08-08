from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    '''New visitor test'''

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        '''check row in table list'''
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'td')
        print(rows)
        self.assertIn(
            row_text, [ row.text for row in rows ]),

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get("http://0.0.0.0:8008")
    
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text

        self.assertIn('To-Do', header_text)
        time.sleep(1)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Купить павлиньи перья')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Купить павлиньи перья')
        
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')

        
        self.fail("End test!")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
