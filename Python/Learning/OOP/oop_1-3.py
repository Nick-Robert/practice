"""
Videos 1-3 covered:
    1) classes vs instances
    2) class variables
    3) classmethods and staticmethods
    
"""

class Employee:

    # class variables
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        # essentially the constructor
        # can define instance variables and also update class variables
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    # Regular methods, accessible through both the class and instance. 
    # Have instance as the first argument automatically (called self by convention)
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # class method, methods which are more about the class itself and not a particular instance
    # Have the class as the first argument (called cls by convention)
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str_1.split('-')
        return cls(first, last, pay)

    # static methods don't take the instance or class as the first argument
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True




emp_1 = Employee('Nick', 'Robert', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# print(Employee.__dict__)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print("-"*10)
emp_1.set_raise_amount(1.05)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print("-"*10)
# when changing class methods, makes more sense to change it by calling the class and not one of its instances 
# (though that also works as shown above)
Employee.set_raise_amount(1.06) # equivalent line: Employee.raise_amt = 1.05
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print("-"*10)


"""
What if you want to create new instances from a given string as in the format below?
"""
# could do this, but requires for the input to be parsed separately from declaring the instance
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)

# instead, could add in another constructor
# see the from_string(...) function in the class, which uses the classmethod as another constructor
new_emp_2 = Employee.from_string(emp_str_2)

"""
Testing static method
"""
import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
