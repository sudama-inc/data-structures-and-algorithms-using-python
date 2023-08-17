"""
115. Write a Python program to check if the elements of a given list are unique or not.

Original list: [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]

Is the said list contains all unique elements!: False

https://www.geeksforgeeks.org/python-check-if-list-contains-all-unique-elements/
"""


lst = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]

flag = 0
for i in range(len(lst)):
    for j in range(len(lst)):
        if i != j:
            if lst[i] == lst[j]:
                flat = 1
print(flag)

if not flag:
    print(True)


# Method 2
def are_elements_unique(lst):
    unique_elements = set(lst)
    return len(unique_elements) == len(lst)


# Example usage
my_list = [1, 2, 3, 4, 5]
result = are_elements_unique(my_list)

if result:
    print("The elements of the list are unique.")
else:
    print("The elements of the list are not unique.")
