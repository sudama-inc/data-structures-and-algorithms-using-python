"""
Polymorphism: Having multiple faces.
Means - When the same thing behaves differently according to the /
/ situation, it is called polymorphism.

1. Method Overriding
2. Method Overloading:
When there are 2 methods in the same class with the same name /
/ but their behavior is different called method overloading.

In that, method executes according to the input arguments.

3. Operator Overloading: Same operator will act differently depending on input.

"""

# ------------------------------------------------------------------------

"""
Abstraction: Hidden. & Force to implement something.
    - A class that hides the implementation details of a concrete class.
    - Apply some constraints.

"""


from abc import ABC, abstractmethod


class BankApp(ABC):

    def database(self):
        print('connected to database')


    @abstractmethod
    def security(self):
        pass

class MobileApp(BankApp):

    def mobile_login(self):
        print('mobile login')

    def security(self):
        print('mobile security')