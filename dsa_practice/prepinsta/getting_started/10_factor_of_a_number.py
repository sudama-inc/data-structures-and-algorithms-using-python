"""
Find the Factors of a Number in Python
Given an integer Number as input, the objective is to search for
all the factors of the Given integer input. Therefore, we write a program
to Find the Factors of a Number in Python Language.

Example
Input : 10
Output : 2 5
"""

"""
Method 1: Using [1, number] as the Range
For an integer input as number, we perform the following operations

Run a while loop for the condition iteration
Check if the number is divisible by the current iter variable.
Increment the iter variable.
Print out all the factors.
"""




import math
def printDivisors(n):
    i = 1
    while i <= n:
        if (n % i == 0):
            print(i, end=" ")
        i += i


# Driver method
printDivisors(10)


"""
Method 2: Using [1, sqrt(number)] as the Range

In this method we’ll use loops to check for factors of a number.
We’ll run a while loop with the condition i<sqrt(number) and check for 
factors within the range.


Run a while loop with condition iter<=sqrt(number).
    Check if the number is divisible by the iter variable.
    increment the iter variable by 1.
    Append the factors if any to the list.
Print out the list containing all the factors.
"""


def printDivisors(n):

    # Note that this loop runs till square root
    i = 1
    while i <= math.sqrt(n):

        if (n % i == 0):

            # If divisors are equal, print only one
            if (n / i == i):
                print(i, end=" ")
            else:
                # Otherwise print both
                print(i, int(n/i), end=" ")
        i = i + 1


# Driver method
printDivisors(10)
