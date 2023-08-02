from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    '''New visitor test'''

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get("http://localhost:8008")
        self.assertIn('To-Do', self.browser.title)
        self.fail("End test!")


if __name__ == "__main__":
    unittest.main(warnings="ignore")