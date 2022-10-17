from django.test import TestCase
from django.test import SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_hodimlar_page_status_code(self):
        response = self.client.get('/hodimlar/')
        self.assertEqual(response.status_code, 200)

    def test_yuldasheva_page_status_code(self):
        response = self.client.get('/yuldasheva/')
        self.assertEqual(response.status_code, 200)

    def test_bulimlar_page_status_code(self):
        response = self.client.get('/bulimlar/')
        self.assertEqual(response.status_code, 200)

