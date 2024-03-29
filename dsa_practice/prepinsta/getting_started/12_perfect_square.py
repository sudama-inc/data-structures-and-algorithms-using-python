"""
Check for Perfect Square in Python
Here on this page, we will learn how to Check for Perfect Square in
Python programming language. We are given an integer number and need
to print “True” if it is, otherwise “False”.

"""

from math import sqrt
import math


"""
Method 1 : Algorithm
Take the floor() value square root of the number.
Multiply the square root twice.
We use the Boolean equal operator to verify if the product of the square root
is equal to the number given.
"""


def isPerfectSquare(x):
    if x >= 0:
        sr = int(sqrt(x))
        return (sr * sr) == x
    return False


n = 84
if isPerfectSquare(n):
    print("True")
else:
    print("False")


"""
Method 2 : Algorithm
In this method we use the floor and ceil function.
If they are equal that implies the number is a perfect square.
"""


def checkperfectsquare(x):
    if (math.ceil(math.sqrt(n)) ==
            math.floor(math.sqrt(n))):
        print("True")
    else:
        print("False")


n = 49
checkperfectsquare(n)
