"""
123. Write a Python program to reverse strings in a given list of string values.

Original lists: ['Red', 'Green', 'Blue', 'White', 'Black']
Reverse strings of the said given list:  ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
https://www.geeksforgeeks.org/python-reverse-all-strings-in-string-list/
https://stackoverflow.com/questions/18686860/reverse-a-string-without-using-reversed-or-1

"""


lst = ['Red', 'Green', 'Blue', 'White', 'Black']
res = []
for i in lst:
    ss = ''
    for s in i:
        ss = s + ss
    res.append(ss)

print(res)


# Reverse a String
def reverse(text):
    lst = []
    count = 1
    for i in range(0, len(text)):
        lst.append(text[len(text)-count])
        count += 1

    lst = ''.join(lst)
    return lst


print(reverse('hello'))


# Reverse a String with another way
def reverse(text):
    s = ""
    l = len(text)
    for i in range(l):
        s += text[l-1-i]
    return s


print(reverse('hello'))
