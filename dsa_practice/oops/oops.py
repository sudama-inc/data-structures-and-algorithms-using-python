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
self
__init__
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