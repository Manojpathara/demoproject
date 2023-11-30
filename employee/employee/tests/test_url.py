from django.test import TestCase

class TestUrl(TestCase):
    def testHomeUrl(self):
        response = self.client.get('/accounts/login/')
        print(response)
        self.assertEqual(response.status_code, 200)