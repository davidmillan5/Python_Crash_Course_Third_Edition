import pytest
from employee import Employee


@pytest.fixture
def based_employee_1():
    """Base employee for the unit test related to the raise of salary"""
    based_employee_1 = Employee('eren', 'jaeger', 50000)
    return based_employee_1


def test_default_raise_of_annual_salary(based_employee_1):
    """Test the correct functionality of the give_raise function without specifying any amount"""
    #based_employee_1 = Employee('eren', 'jaeger', 50000)
    based_employee_1.give_raise()
    assert 55000 == based_employee_1.annual_salary


def test_default_raise_of_annual_salary_specific_value(based_employee_1):
    """Test the correct functionality of the give_raise function without specifying any amount"""
    #based_employee_1 = Employee('eren', 'jaeger', 50000)
    based_employee_1.give_raise(56000)
    assert 106000 == based_employee_1.annual_salary
