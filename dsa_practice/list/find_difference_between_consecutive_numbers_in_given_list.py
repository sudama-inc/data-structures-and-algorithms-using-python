"""
104. Write a Python program to find the difference between consecutive numbers in a given list.

Original list: [1, 1, 3, 4, 4, 5, 6, 7]

Difference between consecutive numbers of the said list: [0, 2, 1, 0, 1, 1, 1]

https://stackoverflow.com/questions/5314241/difference-between-consecutive-elements-in-list

"""

lst = [1, 1, 3, 4, 4, 5, 6, 7]


a = [x - lst[i - 1] for i, x in enumerate(lst) if i > 0]
b = [x - lst[i - 1] for i, x in enumerate(lst)][1:]
c = [t - s for s, t in zip(lst, lst[1:])]

print(a)
print(b)
print(c)