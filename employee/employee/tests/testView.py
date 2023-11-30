from django.test import TestCase, Client
from django.urls import reverse,resolve
from employeeapp.models import  Employee

# class testViews(TestCase):
#     def testHomeViews(self):
#         client = Client()
#         response = client.get(reverse('home'))
#         print(response)
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'home.html')
