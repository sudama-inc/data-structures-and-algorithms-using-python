"""
Encapsulation: Binding of methods and variables

Why Encapsulation? :
By using encapsulation you will give the power to programmer to change/
/ the attribute balues fron outside the class, by using __getattr__ & __setattr__.

__gettr__ : The job of gettr is to display the value of private variables.
__settr__ : The job of settr is to change the value of private variables from outside.

"""

# ----------------------------------------------------------------

"""
Instance Variable? : A variable that has different values for different objects./
/ Its value depends on the object.

Private Attributes:
__balance --> _ATM__balance

"""

# ----------------------------------------------------------------

"""
In Python nothing is truly private, buy why??

In one label you can hide your attributes, but /
/still if you want to change you can change it.


By using a constructor we can't increase the counter
Instance variable is of object & will define inside constructor
But Static variable is of class also it has same value /
/for the instance of all objects. & will define outside of /
constructor of a class. This doesnt have the self as an argument/
/ so will use the @staticmethod as decorator./
/This method calls only using the class not object/
because object needed self as argument.

"""

# ----------------------------------------------------------------

"""
Class Relationship:
1. Aggregation
2. Inheritance

Aggregation (Has-A Relationship): One class owns the other class
When you are creating an object of a class, that object creation /
/process is that you are passing an object of another class /
/as input into the constructor.


"""


# Aggregation (Has-A Relationship)
class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def print_address(self):
        return self.address.get_city(), self.address.pin, self.address.state

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.edit_address(new_city, new_pin, new_state)


class Address:
    def __init__(self, city, pin, state):
        self.__city = city  # TODO: This attribute is private
        self.pin = pin
        self.state = state

    def get_city(self):
        return self.__city

    def edit_address(self, new_city, new_pin, new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state


add1 = Address('bharatpur', 321201, 'rajasthan')
cust = Customer('sudama', 'male', add1)
# print(cust.print_address())

# ----------------------------------------------------------------

"""
Inheritance:
===========================
1. What is Inheritance
2. Examples
3. What gets inherited
===========================

1. Inheritance: Jo aapke papa ka hai wo aapka hai| Code Reusability
You can create classes that inherit from each other. /
/ So you can create a parent class or a child class and because of inheritance/
/ the object of the child class can access both the data and methods of the/
/ parent class.

Note : It has constructor overriding behaviour, so if parent & child/
/ class both has constructor then the attribute from the parent class/
/ will not execute.
Because : Child class override the parent class constructor.
"""


# Parent class
class User:

    def __init__(self):
        self.name = 'Sudama'

    def login(self):
        print("Login Successful")


# Child class
class Student(User):

    def enroll(self):
        print("Enrollment Successful")


u = User()
s = Student()
# print(s.name)
# s.enroll()


"""
What gets inherited?
1. Constructor
2. Non Private Attributes
3. Non Private Methods
"""

'''
Constructor Rules:
1. If child class doesn't have a constructor but Parent class one/
/ the constructor of parent class will be called.
2. If both parent & Child class have the constructor then /
/ constructor of child class will be called and constructor of /
/ the parent class will not be called.
3. Child can't access private members & methods of the parent class.
4. Method Overriding:
If both child and parent class have the same method then method /
/ of child class will be executed. 


"""
super keyword : use to call the same method of parent class.
super() is a way to access the parent class method when parent /
and child has the same method.

super() is always used inside the child class, and can't be used outside the class.
super() can't access variables.
super() only can access the methods.

"""
'''

# 1. Constructor Example
# Only Parent class have the constructor
class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")


# Child class doesn't have a constructor
class SmartPhone(Phone):
    pass


# s = SmartPhone(20000, 'apple', 13)
# s.buy()
# print(s.price)
# print(s.brand)
# print(s.camera)


# 2. Constructor Example
# Parent & Child both class has the constructor
class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera


# Child class doesn't have a constructor
class SmartPhone(Phone):

    def __init__(self, os, ram):
        print("Inside smart phone constructor")
        self.os = os
        self.ram = ram


# s = SmartPhone('Android', 2)


# 3. Child can't access private members & methods of the parent class.
class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def show(self):
        print(self.__price)


# Child class doesn't have a constructor
class SmartPhone(Phone):

    def check(self):
        print(self.__price)


# s = SmartPhone(20000, 'apple', 13)
# s.check()


# Example:
class A:

    def __init__(self):
        self.val1 = 100

    def display1(self, val1):
        print('Class A', self.val1)


class B(A):

    def display2(self, val1):
        print('Class B', self.val1)


# obj = B()
# obj.display1(200)


# 4. Method Overriding
class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('Bubing a Phone')


# Child class doesn't have a constructor
class SmartPhone(Phone):

    def buy(self):
        print('Buying a SmartPhone')
        # Syntax to call parent class buy method
        super().buy()


# s = SmartPhone(20000, 'apple', 13)
# s.buy()

# ----------------------------------------------------------------

# super() --> constructor
class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera


class SmartPhone(Phone):

    def __init__(self, price, brand, camera, os, ram):
        print("Inside smart phone constructor")
        # Note : Called parent constructor from child constructor using super()
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside smart phone constructor")


s = SmartPhone(20000, 'apple', 13, "Android", 2)
print(s.os)
print(s.ram)
print(s.brand)


# ----------------------------------------------------------------

"""
Inheritance in Summary:
1. A class can inherit from another class
2. Inheritance improves code reusability.
3. Constructor, attributes, methods get inherited to the child class.
4. The parent has no access to the child class.
5. Private properties of the parent are not accessible directly in child classes.
6. Child class can override the attributes or methods. This is called overriding.
7. super() is an inbuilt function which is used to invoke the parent /
/ class methods and constructor.
"""