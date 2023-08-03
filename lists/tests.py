from django.test import TestCase

class SmokeTest(TestCase):

    def test_bad_math(self):
        '''Test bad math calculation'''
        self.assertEqual(1 + 1, 3)