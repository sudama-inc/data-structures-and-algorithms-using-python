"""
146. Write a Python program to compute the sum of digits of each number in a given list.
 
Original tuple: [10, 2, 56]
Sum of digits of each number of the said list of integers: 14

https://www.geeksforgeeks.org/python-program-for-sum-the-digits-of-a-given-number/

"""


def getSum(lst):
    sum = 0
    for n in lst:
        while (n != 0):
            sum = sum + (n % 10)
            n = n//10

    return sum


lst = [10, 2, 56]
print(getSum(lst))


# Method 2 : Recursive Approach
def sumDigits(n):
    return 0 if n == 0 else int(n % 10) + sumDigits(int(n / 10))


# Driver code
n = 12345
print(sumDigits(n))
