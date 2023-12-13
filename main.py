# methods = function related to a class
# class vs instance of class

class Employee:
    
    num_of_emps = 0 # increase number of emp by 1 when new emp is created - done in init as init is run everytime a new employee is created
    raise_amount = 1.04 # class variable

    def __init__(self, first, last, pay): #create methods within a class, receives instance as first argument (call self to follow convention)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1 # not "self" as wants class to be consistent for all instances

    def fullname(self): #method
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount) # have to access class variable either through instance or class - alt = self.raise_amount

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # how to take class as first argument - need class methods
    @classmethod # decorator - alterates fx of method, receiving class instead of instance
    def set_raise_amt(cls, amount): # use 'cls" instead of 'class'
        cls.raise_amount = amount

    @classmethod # alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) # create new employee

    @staticmethod # does not need cls or self.
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: # 5 = sat, 6 = sun
            return False
        return True

class Developer(Employee): # creating sub-class, traits inherited from argument 
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang): #add init to add new arguments
        super().__init__(first, last, pay) # pass prev arguments
        # or Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee): 

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def del_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# now when creating instances(self) of classes, can pass through values indicated in init method
# can leave out self, and pass first...

emp_1 = Employee('Clarence', 'Wang', 50000)
emp_2 = Employee('Claire', 'Duong', 60000)

emp_str_1 = 'John-Doe-70000'

new_emp_1 = Employee.from_string(emp_str_1)

dev_1 = Developer('Joel', "Zura", 60000, 'Python')
dev_2 = Developer('Arnie', 'Fen', 50000, 'Java') 

mgr_1 = Manager('Jen', 'Ten', 100000, [dev_1])


# run methods using class names (Makes more obvious what is going on)
Employee.fullname(emp_1) # have to pass instance as argument if using class

Employee.set_raise_amt(1.05) # don't need to pass 'cls' in as it is automatically passed

print(emp_1.fullname()) # using method 2
print(Employee.raise_amount) # "raise_amount" is not accessed from instance but from class. 
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(new_emp_1.email)

print(dev_2.prog_lang)

print(emp_1) # will access str first, if not, then will use repr
# print(repr(emp_1)) can use these 
# print(str(emp_1))

mgr_1.add_emp(dev_2)

mgr_1.print_emps()

import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))

print(isinstance(mgr_1, Employee)) # will check if first arg is instance of 2nd arg
print(issubclass(Manager, Employee))# if a class is a subclass of another

# can change class variables for specific instances: e.g.
    # emp_1.raise_amount = 1.05
    # Therefor, Employee/self.raise_amount can be used distinctly to effect class or instance changes
    # def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        # self.pay = int(self.pay * self.raise_amount)
        # self.raise_amount allows sub-classes to override superclass

# emp_1.fullname()
# Employee.fullname(emp_1)

# you can use class methods to create multiple objects - called constructors


# Class methods vs Static methods
    # static methods do not pass anything automatically
    # e.g. want a function that takes in a particular date and determines if it is a work day
    # if cls or self not accessed in fx, create as static method

# print(help(Developer)) - to see more details re: class


# special methods: will be able to change built in behaviours and special methods:
    # surrounded by "__init__" = Dunder e.g. Dunder Init
    # other common dunder:
        # __repr__(self): -> repr(emp_1) - unambigious representation object used for debugging (used for other devs)
        # __str__(self): -> str(emp_1) - readable representation of object, used a display for user


# property decorators: define a method that can be accessed like an attribute
    # get rid of email attribute in init method
    # @property -> defining email attribute like a method but can be accessed like an attribute
    # def email(self):
        # return '{}.{}@email.com'.format(self.first, self.last)
    # ...
    # print(emp_1.email)


    # Use setter to change first/last/email via below:
    #emp_1.fullname = 'Corey Shafer'

    # @fullname.setter
    # def fullname(self, name):
        # first, last = name.split(' ') # splitting name
        # self.first = first
        # self.last = last

    
    # Deleter
    # @fullname.deleter
    # def fullname(self):
        # print('Delete Name!')
        # self.first = None
        # self.last = None
    # ...
    # del emp_1.fullname