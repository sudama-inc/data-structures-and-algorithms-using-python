"""
77. Write a Python program to count the number of non-empty substrings of a given string.
# Count of non-empty substrings is n*(n+1)/2


https://www.geeksforgeeks.org/count-of-non-empty-sequences-of-a-string/
"""


# Method 1
def number_of_substrings(str):
    str_len = len(str)
    # Count of non-empty substrings is n*(n+1)/2
    return int(str_len * (str_len + 1) / 2)


str1 = input("Input a string: ")
print("Number of substrings:")
print(number_of_substrings(str1))
