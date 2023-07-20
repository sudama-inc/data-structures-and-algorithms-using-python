"""
127. Write a Python program to remove words from a given list of strings
containing a character or string.

Original list: list1: ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
Character list: ['#', 'color', '@']
New list: ['Red', '', 'Green', 'Orange', 'White']


https://www.geeksforgeeks.org/python-remove-words-containing-list-characters/
https://stackoverflow.com/questions/25346058/removing-list-of-words-from-a-string

"""

#  Method 1
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

char_list = ['g', 'o']

res = [ele for ele in test_list if all(ch not in ele for ch in char_list)]

print(res)


# Method 2
querywords = ['What', 'is', 'hello']
stopwords = ['what', 'who', 'is', 'a', 'at', 'is', 'he']

resultwords = [word for word in querywords if word.lower() not in stopwords]
result = ' '.join(resultwords)

print(result)


# Method 3
lst = ['gfg', 'is', 'best', 'for', 'geeks']
char_list = ['g', 'o']

result = []
flag = 1
for i in lst:
    for ch in char_list:
        if ch not in i:
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        result.append(i)
# printing result
print(result)


# Method 4
lst = ['gfg', 'is', 'best', 'for', 'geeks']
char_list = ['g', 'o']

result = []
flag = 1
for i in lst:
    x = i
    for ch in char_list:
        i = i.replace(ch, '')
    if len(i) == len(x):
        result.append(i)
# printing result
print(result)


# Method 5 : Using Recursion


def remove_words(start, lst, charlst, newlist=[]):
    if start == len(lst):
        return newlist
    flag = 0
    for i in charlst:
        if i in lst[start]:
            flag = 1
    if flag == 0:
        newlist.append(lst[start])
    return remove_words(start+1, lst, charlst, newlist)


test_list = ['gfg', 'is', 'best', 'for', 'geeks']
char_list = ['g', 'o']

print(remove_words(0, test_list, char_list))
