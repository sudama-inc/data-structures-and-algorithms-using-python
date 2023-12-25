"""

51. Write a Python program to find the first non-repeating character in a given string.
Write a Python program to find the all non-repeating character in a given string.

Write a Python program to find the first non-repeating WORD in a given string.

https://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/

"""
from collections import Counter

# Nth non-repeating character in a given string
def nth_non_rep_char(st, c):
    non_rep = ''.join([i for i in st if st.count(i) ==1])
    return non_rep[c-1]

st = 'hello'
c = 2
print(nth_non_rep_char(st))


# Method 1
# Try for all non-repeted

def all_non_rep_char(st):
    # non_rep = ''.join([i for i in st if st.count(i) ==1])
    s1 = ''
    for i in st:
        count = st.count(i)
        if count == 1:
            s1 = s1+i
        
    return s1

st = 'hello'
print(all_non_rep_char(st))


# Method 1
# Python program to print the first non-repeating character

string = "gereksgeeks"
index = 0

def first_non_repeating_char(string, index):
    fnc = ""

    if len(string) == 0:
        print("EMTPY STRING")

    for i in string:
        if string.count(i) == 1:
            fnc += i
            break
        else:
            index += 1
    if index == len(string):
        return "All characters are repeating "
    else:
        return (f"First non-repeating character is {fnc} on index {index}")


