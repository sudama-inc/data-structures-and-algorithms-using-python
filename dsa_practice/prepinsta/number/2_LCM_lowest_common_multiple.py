"""
LCM of two numbers in Python
Here, in this section we will discuss the LCM of two numbers in python.
In this Python Program find the LCM of Two Numbers which numbers are entered
by the user. Basically the LCM of two numbers is the smallest number which
can divide the both numbers equally. This is also called Least Common Divisor or LCD.

"""

"""
Method 1 : Algorithm
LCM of two numbers will at least be equal or greater than max(num1, num2)
Largest possibility of LCM will be num1 * num2
When iterating in (i) We can linearly find an (i) that is divisible by both num1 & num2
"""

num1 = 12
num2 = 14
for i in range(max(num1, num2), 1 + (num1 * num2)):
    if i % num1 == i % num2 == 0:
        lcm = i
        break
print(lcm)


"""
Method 2 : Algorithm
Rather than linearly checking for LCM by doing i++. We can do i = i + max
Starting with i = max (num1, num2)
The next possibility of LCM will be ‘max’ interval apart
"""
num1 = 12
num2 = 14
for i in range(max(num1, num2), 1 + (num1 * num2), max(num1, num2)):
    if i % num1 == i % num2 == 0:
        lcm = i
        break

print(lcm)


"""
Method 3 : Algorithm
Initialize HCF = 1
Run a loop in the iteration of (i) between [1, min(num1, num2)]
Note down the highest number that divides both num1 & num2
If i satisfies (num1 % i == 0 && num2 % i == 0) then new value of HCF is i
Use lcm formula :- (num1*num2) / hcf
Print the output
"""
num1 = 12
num2 = 14

# Calculating HCF here
for i in range(1, max(num1, num2)):
    if num1 % i == num2 % i == 0:
        hcf = i

# LCM formula
lcm = (num1*num2)//hcf

print("LCM of", num1, "and", num2, "is", lcm)


"""
Method 4 : Algorithm
Run a while loop until num1 is not equals to num2
If num1>num2 then num1 = num1 – num2
Else num2 = num2 – num1
After the loop ends both num1 & num2 stores HCF
Use LCM formula :- (num1*num2) / hcf
Print Output
"""


def getHCF(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1


num1 = 12
num2 = 14
hcf = getHCF(num1, num2)    # Calculating HCF here
lcm = (num1*num2)//hcf      # LCM formula
print(lcm)


"""
Method 5 : Algorithm
Checked whether any of the input is 0 then return sum of both numbers
If both input are equal return any of the two numbers
If num1 is greater than the num2 then Recursively call findHCF(num1 – num2, num2)
Else Recursively call findHCF(num1, num2-num1)
"""


def getHCF(num1, num2):
    if num1 == 0 or num2 == 0:  # Everything divides 0
        return num1 + num2
    if num1 == num2:         # base case
        return num1
    if num1 > num2:          # num1>num2
        return getHCF(num1 - num2, num2)
    else:
        return getHCF(num1, num2 - num1)


num1 = 12
num2 = 14
hcf = getHCF(num1, num2)        # Calculating HCF here
lcm = (num1*num2)//hcf           # LCM formula

print(lcm)


"""
Method 6 : Algorithm
In Addition, we are using modulo operation to reduce the
number of subtractions required and improve the time complexity

We use repeated Modulo Recursive subtraction (Euclidean Algorithm) to calculate the HCF.
"""


def getHCF(a, b):
    if b == 0:
        return a
    else:
        return getHCF(b, a % b)


num1 = 12
num2 = 14
hcf = getHCF(num1, num2)
lcm = (num1 * num2) // hcf      # LCM formula
print("The hcf is :", lcm)
