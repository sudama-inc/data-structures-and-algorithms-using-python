"""

51. Write a Python program to find the first non-repeating character in a given string.
Write a Python program to find the all non-repeating character in a given string.

Write a Python program to find the first non-repeating WORD in a given string.

https://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/

"""
from collections import Counter

# Method 1
# Try for all non-repeted
st = 'hello'
s1 = ''
for i in st:
    count = st.count(i)
    if count > 1:
        pass
    else:
        s1 = s1+i
print(s1)


# Method 1
# Python program to print the first non-repeating character
string = "geeksforgeeks"
index = -1
fnc = ""

if len(string) == 0:
    print("EMTPY STRING")

for i in string:
    if string.count(i) == 1:
        fnc += i
        break
    else:
        index += 1
if index == len(string)-1:
    print("All characters are repeating ")
else:
    print("First non-repeating character is", fnc)


# Method 2
# Function which repeats first Nonrepeating character
def printNonrepeated(string):
    # Calculating frequencies using Counter function
    freq = Counter(string)
    # Traverse the string
    for i in string:
        if (freq[i] == 1):
            print("First non-repeating character is " + i)
            break


# Driver code
string = "geeksforgeeks"
print(printNonrepeated(string))
