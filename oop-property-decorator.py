class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last


    # here are some examples of a setting a class method to appear as an attribute (an object property decorator)
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)