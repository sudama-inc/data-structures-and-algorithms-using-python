"""
170. Write a Python program to insert an element in a given list after every nth position.

Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

Insert a in the said list after 2 nd element:
[1, 2, 'a', 3, 4, 'a', 5, 6, 'a', 7, 8, 'a', 9, 0]

https://stackoverflow.com/questions/31040525/insert-element-in-python-list-after-every-nth-element
https://www.geeksforgeeks.org/python-append-list-every-nth-index/
https://www.geeksforgeeks.org/python-insert-after-every-nth-element-in-a-list/

"""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Method 1
res = list(''.join(l + 'x' * (n % 3 == 2) for n, l in enumerate(letters)))
print(res)


# Method 2
i = 3
while i < len(letters):
    letters.insert(i, 'x')
    i += 4

print(letters)


# Method 3
n = 4

for i in range(n, len(letters)+n, n+1):
    letters.insert(i, 'X')

print(letters)

# Method 4
test_list = [3, 7, 8, 2, 1, 5, 8, 9, 3]
app_list = 'z'
N = 3

res = []
for idx, ele in enumerate(test_list):
    if idx % N == 0:
        res.append(app_list)
    res.append(ele)

print(res)
