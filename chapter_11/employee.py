class Employee():
    """simulates an employee"""

    def __init__(self, first_name, last_name, salary):
        """initializes first name, last names, and salary as attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raise_amt=5000):
        """raises salary by specified amount ($5000 by default)"""
        self.salary += raise_amt