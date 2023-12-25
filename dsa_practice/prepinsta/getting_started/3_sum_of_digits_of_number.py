"""
Sum of Digits of a Number in Python : Find the sum of the Digits of a Number in Python
Given an input the objective to find the Sum of Digits of a Number in Python.
To do so we’ll first extract the last element of the number and then keep shortening
the number itself.

Example
Input : number = 123
Output : 6

"""

# Method 1: Using Brute Force
num = 123
sum = 0
while num != 0:
    sum += (num % 10)
    num //= 10
print(sum)


n = 123
n_str = list(str(n))
sum = 0
for i in n_str:
    sum += int(i)
print(sum)


# Method 3: Using Recursion II
def findSum(num):
    if num == 0:
        return 0
    return int(num % 10) + findSum(num // 10)


num = 12345
print(findSum(num))


# Method 6: One Line recursive function
def sumDigits(n):
    return 0 if n == 0 else int(n % 10) + sumDigits(int(n // 10))


# Driver code
n = int(input("Enter the number: "))
print(sumDigits(n))
