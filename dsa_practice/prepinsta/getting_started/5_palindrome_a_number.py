"""
Palindrome Program in Python : Check Whether or Not the Number is a Palindrome in Python
Given an integer number as an input, the objective is to check Whether or not the number
is a palindrome. Therefore, we write a code to Check Whether or Not the Number
is a Palindrome in Python Language.

Example
Input : 1221
Output : Palindrome
"""

# Method 1: Using Simple Iteration
num = 1221
temp = num
rev = 0
while num != 0:
    rev = (rev*10)+(num % 10)
    num //= 10
if temp == rev:
    print('Palindrome')
else:
    print('Not Palindrome')


# Method 2: Using String Slicing
num = 1211
reverse = int(str(num)[::-1])


# Method 3: Using Recursion
def recurrev(number, rev):
    if number == 0:
        return rev

    remainder = int(number % 10)
    rev = (rev * 10) + remainder

    return recurrev(int(number / 10), rev)


num = 12321
reverse = 0
reverse = recurrev(num, reverse)
print("Palindrome") if reverse == num else print("Not Palindrome")


"""
Method 4: Using Character matching
For string str iterate on the whole check if we find any condition such that – 

str[i] != str[len(str) - i - 1]
If yes then its not a palindrome
Basically, we are checking ‘i’th character is the same as ‘i’th character from the end or not
"""


def checkPalindrome(str):

    # check if str[i] is same as str[len(str) - i - 1]
    # for whole string
    for i in range(0, len(str)):
        # Basically, we are checking i-th character is
        # same as i-th character from the end or not
        if str[i] != str[len(str) - i - 1]:
            return False

    return True


# main function
s = "kayak"
print("Palindrome") if checkPalindrome(s) else print("Not Palindrome")


"""
Method 5: Using Character matching (Updated)
Working
The logic is same as the previous method with the only difference that –
Rather than iterating on the whole string, we iterate on half of the string input.

Since, if the string is a palindrome, the first half will be the same as the second half from the end.
"""

# we do not need to check the whole string
# only till the mid of string
# as if it palindrome the first half == second half of string when read backwards


def checkPalindrome(str):
    # Run loop from 0 to len/2
    mid = int(len(str) / 2)
    for i in range(0, mid):
        if str[i] != str[len(str) - i - 1]:
            return False

    return True


# main function
s = "kayak"

print("Palindrome") if checkPalindrome(s) else print("Not Palindrome")


"""
Method 6: Using In-Built reversed function
Working
Use the following – reverse = ”.join(reversed(str))
"""


def checkPalindrome(str):
    # using inbuilt reversed function
    reverse = ''.join(reversed(str))
    if str == reverse:
        return True

    return False


# main function
s = "kayak"
print("Palindrome") if checkPalindrome(s) else print("Not Palindrome")


"""
Method 8: Using Flag
The explanation is given in the comments section of the code below
"""
string = "radar"
j = -1
flag = 0
for char in string:
    # char starts from index 0
    # string[j] forces to read from end
    # bcz negative index are read from end
    if char != string[j]:
        flag = 1
        break
    j = j - 1

print(string + " is : ", end="")
print("Not Palindrome") if flag else print("Palindrome")


"""
Method 8: Bonus using backward slicing
We use backward looping/slicing in a for loop here
"""

str1 = "radar"
n = len(str1)
c = []
for i in range(n - 1, -1, -1):
    c.append(str1[i])

rev = "".join(c)

print(str1 + " is: ", end="")
if str1 == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
