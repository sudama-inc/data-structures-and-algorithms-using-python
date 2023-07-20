"""
92. Write a Python program to find string similarity between two given strings.

Original string: Python Exercises && Python Exercises
Similarity between two said strings: 1.0

Hamming distance
Levenshtein distance
Damerau Levenshtein distance
Jaro Winkler distance

https://www.geeksforgeeks.org/python-similarity-metrics-of-strings/
https://stackoverflow.com/questions/17388213/find-the-similarity-metric-between-two-strings
https://huggingface.co/models?pipeline_tag=sentence-similarity&sort=downloads

"""

import difflib


# Method 1
def string_similarity(str1, str2):
    result = difflib.SequenceMatcher(a=str1.lower(), b=str2.lower())
    return result.ratio()


str1 = 'Python Exercises'
str2 = 'Python Exercises'

print(string_similarity(str1, str2))


# Method 2
def compute_similarity(input_string, reference_string):
    diff = difflib.ndiff(input_string, reference_string)
    diff_count = 0
    for line in diff:
        if line.startswith("-"):
            diff_count += 1
    return 1 - (diff_count / len(input_string))


input_string = "Geeksforgeeks"
reference_string = "Geeks4geeks"

print(compute_similarity(input_string, reference_string))
