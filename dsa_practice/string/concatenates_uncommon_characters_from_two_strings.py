"""
70. Write a Python program that concatenates uncommon characters from two strings. 

Description: Two strings are given and you have to modify the 1st string such that all the
common characters of the 2nd string have to be removed and the uncommon characters of the 2nd
string have to be concatenated with the uncommon characters of the 1st string. 

https://www.geeksforgeeks.org/python-string-uncommon-characters/
https://www.geeksforgeeks.org/concatenated-string-uncommon-characters-python/
"""

# Method 1


def uncommon_chars_concat(s1, s2):

    set1 = set(s1)
    set2 = set(s2)

    common_chars = list(set1 & set2)
    result = [ch for ch in s1 if ch not in common_chars] + \
        [ch for ch in s2 if ch not in common_chars]
    return(''.join(result))


s1 = 'abcdpqr'
s2 = 'xyzabcd'
print(uncommon_chars_concat(s1, s2))


# Method 2
def concatenate_uncommon(str1, str2):
    final_str = ''

    # iterating over first string and checking each character is present
    # in the other string or not if not then simply store that character
    # in the variable.
    for i in str1:
        if i in str2:
            pass
        else:
            final_str += i

    for j in str2:
        if j in str1:
            pass
        else:
            final_str += j

    # returning the final string as result
    return final_str


# Driver Code
str1 = 'abcs'
str2 = 'cxzca'
print(concatenate_uncommon(str1, str2))
