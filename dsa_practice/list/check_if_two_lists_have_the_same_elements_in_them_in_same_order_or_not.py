"""
133. Write a Python program to check if two lists have the
same elements in them in same order or not.

Original lists:
['red', 'green', 'black', 'orange']
['red', 'pink', 'green', 'white', 'black']
['white', 'orange', 'pink', 'black']

Test common elements between color1 and color2 are in same order? : True
Test common elements between color1 and color3 are in same order? : False
Test common elements between color2 and color3 are in same order? : False

https://www.geeksforgeeks.org/python-check-if-two-lists-are-identical/

"""

# Initialize the lists
test_list1 = [1, 2, 4, 3, 5]
test_list2 = [1, 2, 4, 3, 5]

result = all(x == y for x, y in zip(test_list1, test_list2))
print(result)


# Method 2
# using sum() + zip() + len() to check if lists are equal
if len(test_list1) == len(test_list2) and len(test_list1) == sum([1 for i, j in zip(test_list1, test_list2) if i == j]):
    print("The lists are identical")
else:
    print("The lists are not identical")
