
"""
***
27. Write a Python program to find the second smallest number in a list.

28. Write a Python program to find the second largest number in a list.
***(change the Sing of < to >)

"""


def Range(list1):
    lowest = list1[0]
    lowest2 = None
    for item in list1[1:]:
        if item < lowest:
            lowest2 = lowest
            lowest = item
        elif lowest2 is None or lowest2 > item:
            lowest2 = item

    print("Smallest element is:", lowest)
    print("Second Smallest element is:", lowest2)


# Driver Code
list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
Range(list1)


def second_smallest(numbers):
    m1 = m2 = float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2


print(second_smallest([1, 2, 3, 4]))


def secsmall(numbers):
    small = max(numbers)
    for i in range(len(numbers)):
        if numbers[i] > min(numbers):
            if numbers[i] < small:
                small = numbers[i]
    return small


print(secsmall([1, 2, 3, 4]))


def second_smaller(numbers):
    # if len(numbers)<2: return None or otherwise raise an exception

    m1, m2 = numbers[:2]
    if m2 < m1:
        m1, m2 = m2, m1

    for x in numbers[2:]:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2


print(second_smaller([1, 2, 3, 4]))
