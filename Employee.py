class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



emp_1 = Employee("Eric", "Kim", 50000)
emp_2 = Employee("Test", "User", 60000)

import datetime
my_date = datetime.date(2023, 5, 27)

print(Employee.is_workday(my_date))

"""
emp_str_1 = "eas-adsa-2213"
emp_str_2 = "afd-dfaf-2323"
emp_str_3 = "gege-sdfs-2543"

new_emp_1 = Employee.from_string(emp_str_1)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
"""