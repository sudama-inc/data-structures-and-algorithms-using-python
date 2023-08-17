"""
184. Write a Python program to generate Bigrams of words from a given list of strings.

From Wikipedia:
A bigram or digram is a sequence of two adjacent elements from a string of tokens,
which are typically letters, syllables, or words. A bigram is an n-gram for n=2.
The frequency distribution of every bigram in a string is commonly used for simple
statistical analysis of text in many applications, including in computational linguistics,
cryptography, speech recognition, and so on.


Original list:
['Sum all the items in a list', 'Find the second smallest number in a list']
Bigram sequence of the said list:
[('Sum', 'all'), ('all', 'the'), ('the', 'items'), ('items', 'in'), ('in', 'a'),
('a', 'list'), ('Find', 'the'), ('the', 'second'), ('second', 'smallest'),
('smallest', 'number'), ('number', 'in'), ('in', 'a'), ('a', 'list')]

https://www.geeksforgeeks.org/python-bigram-formation-from-given-list/
https://stackoverflow.com/questions/21844546/forming-bigrams-of-words-in-list-of-sentences-with-python
"""

# Method 1 : Simple Iteration
lst = ['Sum all the items in a list',
       'Find the second smallest number in a list']

res = []
for item in lst:
    res.extend(item.split())
print(res)

result = []
for i in range(len(res)-1):
    result.append((res[i], res[i+1]))
print(result)


# Method 5
ans = []
text = ['cant railway station', 'citadel hotel', ' police stn']
for line in text:
    arr = line.split()
    for i in range(len(arr)-1):
        ans.append((arr[i], arr[i+1]))

print(ans)


# Method 2
result = [a for ls in lst for a in zip(ls.split(" ")[:-1], ls.split(" ")[1:])]


# Method 3
res = [(x, i.split()[j + 1])
       for i in lst for j, x in enumerate(i.split()) if j < len(i.split()) - 1]


# Method 4
res = [i for j in lst
       for i in zip(j.split(" ")[:-1], j.split(" ")[1:])]
