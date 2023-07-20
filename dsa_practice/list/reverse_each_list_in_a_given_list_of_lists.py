"""
***
129. Write a Python program to reverse each list in a given list of lists.
150. Write a Python program to reverse a given list of lists.

Original list of lists:
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Reverse each list in the said list of lists:
[[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]

https://stackoverflow.com/questions/3940128/how-do-i-reverse-a-list-or-loop-over-it-backwards
https://www.geeksforgeeks.org/python-reversing-list/
"""


def rev_manual_pos_gen(mylist):
    max_index = len(mylist) - 1
    return [mylist[max_index - index] for index in range(len(mylist))]


def rev_manual_neg_gen(mylist):
    # index is 0 to 9, but we need -1 to -10
    return [mylist[-index-1] for index in range(len(mylist))]


def rev_manual_index_loop(mylist):
    a = []
    reverse_index = len(mylist) - 1
    for index in range(len(mylist)):
        a.append(mylist[reverse_index - index])
    return a


def rev_manual_loop(mylist):
    a = []
    reverse_index = len(mylist)
    for index, _ in enumerate(mylist):
        reverse_index -= 1
        a.append(mylist[reverse_index])
    return a


mylist = [1, 2, 3, 4]

# Using List Comprehension
original_list = [10, 11, 12, 13, 14, 15]
new_list = [original_list[len(original_list) - i]
            for i in range(1, len(original_list)+1)]
print(new_list)


# Using Append Function
lst = [1, 2, 3, 4, 5]
reversed_lst = []
for i in range(len(lst)-1, -1, -1):
    reversed_lst.append(lst[i])
print(reversed_lst)


"""
*** Reversing a list using two-pointer approach ***
"""


def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while (left < right):
        # Swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(arr))
