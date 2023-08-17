"""
Prime Number Program in Python : Check Whether a Number is a Prime or Not in Python
Given an integer input the objective is to write a program to Check Whether a Number is a Prime or Not in Python Language.

Example
Input : 11
Output : 11 is a Prime


Explanation : Given an integer input for a number, the objective is to check whether
or not the number is a prime. In order to do so we keep checking with all the numbers
until square root of the number itself for factors of the number input. If found any,
the number is not a prime. Here are some of the methods given to solve the above
mentioned problem in python language.


Method 1: Simple iterative solution
Method 2: Optimization by break condition
Method 3: Optimization by n/2 iterations
Method 4: Optimization by √n
Method 5: Optimization by skipping even iteration
Method 6: Basic Recursion technique
"""

# Method 1: Simple iterative solution
num = 15
flag = 0
for i in range(2, num):
    if num % i == 0:
        flag = 1
        break
if flag == 1:
    print('Not Prime')
else:
    print("Prime")


# Method 2: Optimization by break condition
num = 15
flag = 0
if num < 2:
    flag = 1
else:
    for i in range(2, int((num/2)+1)):
        if num % i == 0:
            flag = 1
            break

if flag == 1:
    print('Not Prime')
else:
    print("Prime")


# Method 4: Optimization by √n
num = 7
flag = 0
if num < 2:
    flag = 1
else:
    for i in range(2, int(pow(num, 0.5)+1)):
        if num % i == 0:
            flag = 1
            break

if flag == 1:
    print('Not Prime')
else:
    print("Prime")


# Method 5: Optimization by skipping even iteration
num = 15
flag = 0
if num < 2:
    flag = 1
elif num == 2:
    flag = 0
else:
    for i in range(3, int(pow(num, 0.5)+1), 2):
        if num % i == 0:
            flag = 1
            break

if flag == 1:
    print('Not Prime')
else:
    print("Prime")


"""
Print all prime numbers in an interval.
"""
lower = 10
upper = 50
for num in range(lower, upper+1):
    # all prime numbers are greater then 1
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                break
        else:
            print(num)
