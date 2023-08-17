"""
Factorial of a Number in Python
Here we will discuss how to find the Factorial of a Number in Python programming language.

Factorial of any number is the product of it and all the positive numbers
below it for example factorial of 5 is 120

Factorial of n (n!) = 1 * 2 * 3 * 4....n
5! = 1 x 2 x 3 x 4 x 5 = 120 7! = 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5040

"""

# Method 1 (Iterative)
num, fact = 6, 1
# Factorial of negative number doesn't exist
if num < 0:
    print("Not Possible")
else:
    for i in range(1, num+1):
        fact = fact * i
print(fact)


# Method 2 (Recursive)
def getFactorial(num):
    if num == 0:
        return 1

    return num * getFactorial(num - 1)


num = 6
print(getFactorial(num))
