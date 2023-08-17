"""
***
66. Write a Python program to make two given strings (lower case, may or may not be
the same length) anagrams without removing any characters from any of the strings.


https://www.geeksforgeeks.org/python-sorted-check-two-strings-anagram-not/
https://stackoverflow.com/questions/14990725/how-can-i-check-if-two-strings-are-anagrams-of-each-other
"""

from collections import Counter


# Method 1
def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)


# Method 2
def anagram(s):
    string_list = []
    for ch in s.lower():
        string_list.append(ch)

    print('string_list : ', string_list)

    string_dict = {}
    for ch in string_list:
        if ch not in string_dict:
            string_dict[ch] = 1
        else:
            string_dict[ch] += 1

    return string_dict


s1 = "master"
s2 = "stream"

a = anagram(s1)
b = anagram(s2)

if a == b:
    print("Anagram")
else:
    print("Not Anagram")


# Method 3
def isanagram2(wrd1, wrd2):
    wrd1_dict = {k: 0 for k in wrd1}
    wrd2_dict = {k: 0 for k in wrd2}

    for c1, c2 in zip(wrd1, wrd2):
        wrd1_dict[c1] += 1
        wrd2_dict[c2] += 1

    if wrd1_dict == wrd2_dict:
        return True
    return False
