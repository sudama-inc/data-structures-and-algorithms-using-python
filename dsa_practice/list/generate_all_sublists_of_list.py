
"""
33. Write a Python program to generate all sublists of a list.

https://www.geeksforgeeks.org/python-print-sublists-list/

Step 1: Run a loop till length+1 of the given list.
Step 2: Run another loop from 0 to i.
Step 3: Slice the subarray from j to i. 
Step 4: Append it to a another list to store it 
Step 5: Print it at the end

"""


def sub_lists(l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists


# driver code
l1 = [1, 2, 3]
print(sub_lists(l1))


def generateSublists(lst):
    # Base case
    if len(lst) == 0:
        return [[]]

    # Recursive case
    sublists = []
    first_element = lst[0]
    rest_list = lst[1:]
    sublists_of_rest = generateSublists(rest_list)

    # Generate sublists including first element
    for sublist in sublists_of_rest:
        sublists.append([first_element] + sublist)
    # Generate sublists excluding first element
    sublists.extend(sublists_of_rest)

    return sublists


# Driver code
l1 = [1, 2, 3]
print(generateSublists(l1))
