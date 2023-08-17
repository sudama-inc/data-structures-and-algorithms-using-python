"""
116. Write a Python program to sort a list of lists by a given index of the inner list.

Original list: [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), 
                ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

Sort the said list of lists by a given index ( Index = 0 ) of the inner list: 
[('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), 
('Wyatt Knott', 91, 94)]

https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
"""

from operator import itemgetter

lst = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96),
       ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

lst.sort(key=lambda x: x[0])

print(lst)

result = sorted(lst, key=itemgetter(0))
