from django.test import TestCase
from django.urls import reverse, resolve
from employeeapp.views import home

class TestUrlReverse(TestCase):
    def testHomeUrl(self):
        url = reverse('home')
        print("resolve: ", resolve(url))
        self.assertEqual(resolve(url).func, home)