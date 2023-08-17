"""
Reverse a Number in Python : Find the Reverse of a Number in Python
Given an integer input the objective is to reverse the given integer
number using loops and slicing. Therefore, we’ll write a program to
Find the Reverse of a Number in Python Language.

Example
Input : 123
Output : 321
"""


# Method 1: Using Simple Iteration
"""
Run a while loop with the condition number >0.
Extract the last digit as Remainder using Modulo operator.
Using the formula reverse = ( reverse * 10 ) + remainder , we keep changing the reverse value.
Break down the Nunber using divide operator.
Print the reverse variable.
"""
num = 1234
rev = 0
while num != 0:
    rev = (rev*10)+(num % 10)
    num //= 10
print(rev)


# Method 2: Using String Slicing
st = str(num)
print(st[::-1])


# Method 3: One Line recursive function
def recursum(number, reverse):
    if number == 0:
        return reverse
    remainder = int(number % 10)
    reverse = (reverse*10)+remainder
    return recursum(int(number/10), reverse)


num = 1234
reverse = 0
print(recursum(num, reverse))
