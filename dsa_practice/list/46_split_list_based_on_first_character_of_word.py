
"""
40. Write a Python program to split a list based on the first character of a word.

"""


def splitLst(x):
    dictionary = dict()
    for word in x:
        f = word[0]
        if f in dictionary.keys():
            dictionary[f].append(word)
        else:
            dictionary[f] = [word]
    return dictionary

lst = ['About', 'Are', 'As', 'At', 'Aunt', 'Aw', 'Bedlam',  'Bill', 'Billgone', 'cat', 'dict']
print(splitLst(lst))
