"""
157. Write a Python program to interleave lists of varying lengths.

Original lists:
[2, 4, 7, 0, 5, 8]
[2, 5, 8]
[0, 1]
[3, 3, -1, 7]

Interleave said lists of different lengths: [2, 2, 0, 3, 4, 5, 1, 3, 7, 8, -1, 0, 7, 5, 8]

https://www.geeksforgeeks.org/python-interleave-multiple-lists-of-same-length/
https://www.geeksforgeeks.org/python-interleave-two-lists-of-different-length/
https://stackoverflow.com/questions/48199961/how-to-interleave-two-lists-of-different-length
"""


# Method 1
def twolists(list1, list2, list3, list4):
    newlist = []
    a1 = len(list1)
    a2 = len(list2)
    a3 = len(list3)
    a4 = len(list4)

    for i in range(max(a1, a2)):
        if i < a1:
            newlist.append(list1[i])
        if i < a2:
            newlist.append(list2[i])
        if i < a3:
            newlist.append(list3[i])
        if i < a4:
            newlist.append(list4[i])

    return newlist


l1 = [2, 4, 7, 0, 5, 8]
l2 = [2, 5, 8]
l3 = [0, 1]
l4 = [3, 3, -1, 7]
print(twolists(l1, l2, l3, l4))


# 2 Pointer Approch for Same length of the list
def interleave_lists(list1, list2):
    # Initialize the result list and pointers for both lists
    result = []
    i = 0
    j = 0
    # Continue the loop as long as either list has unprocessed elements
    while i < len(list1) or j < len(list2):
        # If the first list has unprocessed elements, append the next element
        if i < len(list1):
            result.append(list1[i])
            i += 1
        # If the second list has unprocessed elements, append the next element
        if j < len(list2):
            result.append(list2[j])
            j += 1
    return result


# initializing lists
test_list1 = [1, 4, 5]
test_list2 = [3, 8, 9]
res = interleave_lists(test_list1, test_list2)
print(res)
