"""
10. Write a Python program to change a given string to a newly string where the
first and last chars have been eiixchanged.
'abcd' --> 'dbca'

https://www.geeksforgeeks.org/python-program-to-swap-the-first-and-the-last-character-of-a-string/
"""

# Method 1


def change_sring(str1):
    return str1[-1:] + str1[1:-1] + str1[:1]


print(change_sring('abcd'))


# Method 2
