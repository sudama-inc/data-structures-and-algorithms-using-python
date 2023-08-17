"""
Find the Fibonacci Series up to Nth Term in Python
Given an integer as an input, the objective is to find the Fibonacci series until the number input as the Nth term. Therefore, we write a program to Find the Fibonacci Series up to Nth Term in Python Language.

Example
Input : 4
Output : 0 1 1 2

"""

# Method 1: Using Simple Iteration
import math
num = 10
n1, n2 = 0, 1
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()


# Method 2: Using Recursive Function
def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))


num = 10
if num <= 0:
    print("Please enter a Positive Number")
else:
    print("Fibonacci Series:", end=" ")
for i in range(num):
    print(fibonacciSeries(i), end=" ")


# Method 3 : Direct formula to find nth term of Fibonacci Series
# Fn = {[(√5 + 1)/2] ^ n} / √5


def fibonacciSeries(phi, n):
    for i in range(0, n + 1):
        result = round(pow(phi, i) / math.sqrt(5))
        print(result, end=" ")


num = 10
phi = (1 + math.sqrt(5)) / 2
fibonacciSeries(phi, num)


# Method 4 : For Nth Item
def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Test the function
n = 3
print(fibonacci(n))
