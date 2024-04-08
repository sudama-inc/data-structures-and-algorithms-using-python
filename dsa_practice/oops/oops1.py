"""
Coding Principles
DRY = Don't Repeat Yourself.
Don't Repeat Yourself (DRY) is a software engineering practice that /
/allows you to write code that is easier to read and understand.

Ek baar likho baar baar use kro.
"""


"""
Everything in Python is an Object

Object: Object is an instance of a class

Class: Its a Blueprint
1. Data or Property
2. Functions or Behavior

# Syntax to create an Object
# objectname = classname()

2 Types of classes their in Python
1. BuiltIn Class
2. User Defined Class

"""


"""
Constructor : Constructor is a function inside a class.
Constructor (Special Function) --> To execute the code inside of constructor /
/No Need to Call This Function Explictly
1. __init__ : It allows you to initialize the attributes (variables) of an object.
It used to write configuration related code.
It doesn't gives the control to the end user.
It automatically trigers when the class calls.

What is the benifit of the constructer (__init__)??
It ensures objects are properly initialized, promotes encapsulation and modular design,/
/facilitates dependency injection, allows customization of initialization logic,/
/and contributes to writing readable and maintainable code.

Initialization
Encapsulation
Self-reference 
Dependency Injection
Default Values
Customization
Readable and Maintainable Code
Inheritance

2. self --> It nothing but a current object of the class . (classboject)
classboject = classname()
self & classboject has the same memory address.

Why do we need self?
It is used to access the attributes of the object.
Also in class one function can't communicate with other function So /
/self the the medium to communicate the with other function.
self is the conviction name you can name it with any name.

class object only have the access for its attributes and methods / 
so methods cant communicate with each other thats why we need self.

"""

#----------------------------------------------------------------

"""
Oop's Concepts:

Abstraction
Encapsulation
Inheritance
Polymorphism
"""

"""
Methods Vs Functions
Methods: Method is create inside the class.
Functions: Functions is createed independently or outside the class.
"""

"""
Magic (Dunder) Methods:
__init__: This method is called when a new object is created. It is used to initialize the object's attributes.
__new__: This method is called before __init__. It is used to create a new object instance.
__del__: This method is called when an object is destroyed. It is used to clean up any resources that the object is using.
__str__: This method is called when an object is converted to a string. It is used to return a string representation of the object.
__repr__: This method is called when an object is represented in a REPL (read-eval-print loop). It is used to return a string representation of the object that can be used to recreate the object.
__len__: This method is called when the len() function is used on an object. It is used to return the length of the object.
__getitem__: This method is called when the [] operator is used on an object. It is used to get the value at a specified index in the object.
__setitem__: This method is called when the [] operator is used to set the value at a specified index in the object.
__add__: This method is called when the + operator is used on an object. It is used to add two objects together.
__sub__: This method is called when the - operator is used on an object. It is used to subtract two objects.
__mul__: This method is called when the * operator is used on an object. It is used to multiply two objects.
__truediv__: This method is called when the / operator is used on an object. It is used to divide two objects.
__floordiv__: This method is called when the // operator is used on an object. It is used to perform integer division on two objects.
__mod__: This method is called when the % operator is used on an object. It is used to return the remainder of the division of two objects.
__pow__: This method is called when the ** operator is used on an object. It is used to raise an object to a power.

"""


#----------------------------------------------------------------


class Atm:

    def __init__(self):
        self.pin = None
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
            Hi how can I help you?
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check balance
            4. Press 4 to withdraw
            5. Anything else to Exit            
            """)

        if user_input == "1":
            # create pin
            self.create_pin()
        elif user_input == "2":
            # change pin
            self.change_pin()
        elif user_input == "3":
            # check balance
            self.check_balance()
        elif user_input == "4":
            # withdraw
            self.withdraw()
        else:
            exit()


    def create_pin(self):
        self.pin = input("Enter your pin: ")
        self.balance = int(input("Enter Balance: "))

        print("Pin Created Successfully")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter old pin: ")
        new_pin = input("Enter new pin: ")

        if old_pin == self.pin:
            self.pin = new_pin
            print("Pin Changed Successfully")
            self.menu()
        else:
            print("Old pin is incorrect")
            print("Please try again")
            self.menu()


    def check_balance(self):
        user_pin = input("Please enter: ")
        if user_pin == self.pin:
            print("Balance: ", self.balance)
        else:
            print("Pin is incorrect")
            print("Please try again")
            self.menu()
            self.check_balance()

        print("Balance: ", self.balance)
        self.menu()


    def withdraw(self):
        user_pin = input("Please enter: ")
        if user_pin == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Amount Withdrawn Successfully")
                self.menu()
            else:
                print("Insufficient Balance")
                self.menu()
        else:
            print("Pin is incorrect")
            print("Please try again")
            self.menu()
            self.check_balance()

        print("Balance: ", self.balance)
        self.menu()


obj = Atm()