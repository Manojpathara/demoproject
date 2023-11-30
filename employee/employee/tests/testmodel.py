from django.test import TestCase
from employeeapp.models import Employee

class TestModel(TestCase):
    def testModelEmployee(self):
        emp = Employee.objects.create(name="varun",address ="kerala", age=22)
        self.assertIsInstance(emp, Employee)