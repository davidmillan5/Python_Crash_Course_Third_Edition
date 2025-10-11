"""Class to create instances of employees with first name, last name and annual salary"""

class Employee:
    """Class to create instances of employees"""

    def __init__(self,first_name,last_name,annual_salary):
        """Create an instance of the class employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self,raise_amount=None):
        """Give an automatic raise adding $5,0000"""
        if raise_amount:
            self.annual_salary += raise_amount
            return self.annual_salary
        else:
            self.annual_salary +=5000
            return self.annual_salary

