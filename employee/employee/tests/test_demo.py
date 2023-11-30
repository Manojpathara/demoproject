from django.test import TestCase

def get_max(num1,num2):
    return num1 if num1 > num2 else num2
class testDemo(TestCase):
    def test_get_max(self):
        self.assertEqual(get_max(5,8),8)