"""
Armstrong Number in Python
Check Whether a Given Number is an Armstrong Number or Not in Python
For a given integer the objective is to check whether or not the given integeris an
Armstrong number or not. The Armstrong number is briefly defined in the section below.

Example
Input : 371
Output : It's an Armstrong Number

Armstrong Number: In order to do so, we check whether the sum of the digits of
each number to the power the length of the number is equal to the number itself
or not. If the number is the same as the original, it’s an Armstrong number. 
Mentioned below are a few of the Methods used to solve this problem,

"""

"""
Method 1: Using Iteration
In this method we’ll use for loop and while loop to check for Armstrong number.

Working : For an integer input number, we perform the following operations

We break down the number into digits using “%” operator.
We raise the digit to the power of the length of the number.
Keep appending the value to sum variable.
Check if the sum variable matches the number itself.
If the above condition is satisfied, it’s an Armstrong Number.
"""

number = 371
num = number
digit, sum = 0, 0
length = len(str(num))
for i in range(length):
    digit = int(num % 10)
    num = num/10
    sum += pow(digit, length)
if sum == number:
    print("Armstrong")
else:
    print("Not Armstrong")


"""
Method 2: Using Recursion
In this method we’ll use recursion to check for Armstrong number. To know more about recursion, check out Recursion in Python.

Working : For a given integer input, we do the following

Define a recursive function checkArmstrong() with base case as num==0.
Set the recursive step call as checkArmstrong(num/10, length, sum).
"""

number = 371
num = number
sum = 0
length = len(str(num))


def checkArmstrong(num, length, sum):
    if num == 0:
        return sum
    sum += pow(int(num % 10), length)
    return checkArmstrong(num/10, length, sum)


if checkArmstrong(num, length, sum) == number:
    print('Armstrong')
else:
    print("Not Armstrong")
