"""
***
4. Write a Python program to get a string from a given string where all occurrences
of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'


https://www.geeksforgeeks.org/python-replace-occurrences-by-k-except-first-character/
"""

# Method 1
st = 'restart'
k = '$'
s = ''

for i in st:
    if i == st[0] and i not in s:
        s += i
    elif i == st[0] and i in s:
        s += k
    else:
        s += i
print(s)


# Method 2
test_str = 'restart'
K = '$'
x = ""
for idx, char in enumerate(test_str):
    if idx == 0:
        x += char
    else:
        x += K if char == test_str[0] else char

print(x)
