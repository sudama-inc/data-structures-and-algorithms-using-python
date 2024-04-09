"""
Types of Inheritance:
1. Single Inheritance
2. Multilevel Inheritance
3. Hierarchical Inheritance
4. Multiple Inheritance (Diamond / Ambiguity Problem)
5. Hybrid Inheritance
"""

# ----------------------------------------------------------------


# 1. Single Inheritance:
class Phone:

    def __init__(self, price, brande, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brande
        self.camera = camera

    def buy(self):
        print('Bubing a Phone')


class SmartPhone(Phone):
    pass

#
# s = SmartPhone(20000, "apple", 13)
# s.buy()

# ----------------------------------------------------------------


# 2. Multilevel Inheritance:
class Product:

    def review(self):
        print("Product customer review")


class Phone(Product):

    def __init__(self, price, brande, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brande
        self.camera = camera

    def buy(self):
        print('Bubing a Phone')


class SmartPhone(Phone):
    pass


# s = SmartPhone(20000, "apple", 13)
# s.buy()
# s.review()

# ----------------------------------------------------------------


# 3. Hierarchical Inheritance:
class Phone(Product):

    def __init__(self, price, brande, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brande
        self.camera = camera

    def buy(self):
        print('Bubing a Phone')


class SmartPhone(Phone):
    pass


class FeaturePhone(Phone):
    pass


# s = SmartPhone(20000, "apple", 13)
# s.buy()
# s = FeaturePhone(200, "lava", 1)
# s.buy()

# ----------------------------------------------------------------


# 4. Multiple Inheritance (Diamond / Ambiguity Problem):
class Phone:

    def __init__(self, price, brande, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brande
        self.camera = camera

    def buy(self):
        print('Bubing a Phone')


class Product:
    def review(self):
        print("Product customer review")


class SmartPhone(Phone, Product):
    pass


s = SmartPhone(20000, "apple", 13)
s.buy()
s.review()

# ----------------------------------------------------------------


# *** Diamond / Ambiguity Problem:

class Phone:

    def __init__(self, price, brande, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brande
        self.camera = camera

    def buy(self):
        print('Bubing a Phone')


class Product:
    def buy(self):
        print("Product by method")


# Method Resolution Order (MRO)
class SmartPhone(Phone, Product):
    pass


s = SmartPhone(20000, "apple", 13)
s.buy()