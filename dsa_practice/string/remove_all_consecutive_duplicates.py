"""
67. Write a Python program to remove all consecutive duplicates of a given string.


106. Write a Python program to remove repeated consecutive characters and replace
them with single letters and print a updated string.

Sample Data:
("Red Green White") -> "Red Gren White"
("aabbbcdeffff") -> "abcdef"
("Yellowwooddoor") -> "Yelowodor"

https://www.geeksforgeeks.org/remove-consecutive-duplicates-string/
https://www.geeksforgeeks.org/python-replace-multiple-occurrence-of-character-by-single/
"""


from itertools import groupby


# Method 1
def remove_all_consecutive(str1):
    result_str = []
    for (key, group) in groupby(str1):
        result_str.append(key)

    return ''.join(result_str)


str1 = 'xxxyyyyxxxyyyxxxyyyy'
print(remove_all_consecutive(str1))


# Method 2
def delete_consecutive_strings(s):

    # Initialize Start and Stop Pointers.
    i = 0
    j = 0
    new_elements = ''

    # Iterate String Using j pointer.
    while (j < len(s)):
        # If both elements are same then skip.
        if (s[i] == s[j]):
            j += 1
    # If both elements are not same then append new element.
        elif ((s[j] != s[i]) or (j == len(s)-1)):
            new_elements += s[i]

    # After appending sliding over the window.
            i = j
            j += 1
    # Append the last string.
    new_elements += s[j-1]
    return new_elements


s = 'geeks for geeks is best'
print(delete_consecutive_strings(s))


# Method 3
def removeConsecutiveDuplicates(s):
    if len(s) < 2:
        return s
    if s[0] != s[1]:
        return s[0]+removeConsecutiveDuplicates(s[1:])
    return removeConsecutiveDuplicates(s[1:])


s1 = 'geeksforgeeks'
print(removeConsecutiveDuplicates(s1))


# Method 4
def removeDuplicates(S):
    n = len(S)
    if (n < 2):
        return
    # j is used to store index is result string
    # (or index of current distinct character)
    j = 0

    # Traversing string
    for i in range(n):
        # If current character S[i] is different from S[j]
        if (S[j] != S[i]):
            j += 1
            S[j] = S[i]

    # Putting string termination character.
    j += 1
    S = S[:j]
    return S


# Driver Code
if __name__ == '__main__':

    S1 = "geeksforgeeks"
    S1 = list(S1.rstrip())
    S1 = removeDuplicates(S1)
    print(*S1, sep="")


# Method 1
def test(text):
    result = []
    for x in text:
        if not result or result[-1] != x:
            result.append(x)
    return ''.join(result)


text = "aabbbcdeffeeff"
print(test(text))
