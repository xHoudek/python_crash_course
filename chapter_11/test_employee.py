import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """tests for the class Employee"""

    def setUp(self):
        """create an employee for use in all test methods"""
        self.my_employee = Employee('Homer', 'Simpson', 60000)

    def test_give_default_raise(self):
        """tests the give_raise method using the default value of $5000"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 65000)

    def test_give_custom_raise(self):
        """tests the give_raise method using a custom value of $23"""
        self.my_employee.give_raise(23)
        self.assertEqual(self.my_employee.salary, 60023)

unittest.main()