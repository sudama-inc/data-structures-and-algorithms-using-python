"""
48. Write a Python program to swap commas and dots in a string.
Sample string: "32.054,23"
Expected Output: "32,054.23"

https://www.geeksforgeeks.org/python-swap-commas-dots-string/
"""


# Python code to replace, with . and vice-versa
def Replace(str1):
    arr = []

    for i in str1:
        if (i == '.'):
            arr.append(',')
        elif (i == ','):
            arr.append('.')
        else:
            arr.append(i)
    str2 = ''.join(arr)
    return str2


# Driving Code
string = "14,625,498.002"
print(Replace(string))
