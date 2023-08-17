"""
HCF of Two Numbers
Here, in this section we will discuss how to find HCF of two numbers in python. HCF means (Highest Common Factor) also known as GCD (Greatest Common Divisor).

x is called HCF of a & b two conditions :

x can completely divide both a & b leaving remainder 0
No, other number greater than x can completely divide both a & b

"""


"""
Method 1 : Linear Quest Algorithm
Initialize HCF = 1
Run a loop in the iteration of (i) between [1, min(num1, num2)]
Note down the highest number that divides both num1 & num2
If i satisfies (num1 % i == 0 and num2 % i == 0) then new value of HCF is i
Print value of HCF
"""
num1 = 36
num2 = 60
hcf = 1

for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print(hcf)


"""
Method 2 : Repeated Subtraction Algorithm
Run a while loop until num1 is not equals to num2
If num1>num2 then num1 = num1 – num2
Else num2 = num2 – num1
After the loop ends both num1 & num2 stores HCF
"""
num1 = 36
num2 = 60
a = num1
b = num2

while num1 != num2:
    if num1 > num2:
        num1 -= num2
    else:
        num2 -= num1

print(num1)


"""
Method 3 : Repeated Subtraction using Recursion
Algorithm
Checked whether any of the input is 0 then return sum of both numbers
If both input are equal return any of the two numbers
If num1 is greater than the num2 then Recursively call findHCF(num1 – num2, num2)
Else Recursively call findHCF(num1, num2-num1)
"""
# Recursive function to return HCF of two number


def findHCF(num1, num2):
    if num1 == 0 or num2 == 0:  # Everything divides 0
        return num1 + num2
    if num1 == num2:            # base case
        return num1
    if num1 > num2:             # num1>num2
        return findHCF(num1 - num2, num2)
    else:
        return findHCF(num1, num2 - num1)


num1 = 36
num2 = 60
print(findHCF(num1, num2))


"""
Method 4 : Repeated Subtraction with Modulo Operator using Recursion Algorithm
If b is equals to 0 return a
Else recursively call the function for value b, a%b and return 
"""


def getHCF(a, b):
    return b == 0 and a or getHCF(b, a % b)


num1 = 36
num2 = 60
print(getHCF(num1, num2))


"""
Method 5 : Handling Negative Numbers in HCF
If any of the number is negative then convert it to positive by multiplying
it with -1 as according to the proper definition HCF of two numbers can never be negative.

If b is equals to 0 return a
Else recursively call the function for value b, a%b and return 

"""


def getHCF(a, b):
    return b == 0 and a or getHCF(b, a % b)


num1 = -36
num2 = 60
num1 >= 0 and num1 or -num1
num2 >= 0 and num2 or -num2
print(getHCF(num1, num2))


