"""
Count Consecutive Zeros with their First and Last Index

"""


def find_consecutive_zeros(lst):
    result = []
    count = 0
    start_index = None

    for i, num in enumerate(lst):
        if num == 0:
            if count == 0:
                start_index = i
            count += 1
        elif count > 0:
            end_index = i - 1
            result.append({'count': count, 'starting_index': start_index, 'ending_index': end_index})
            count = 0

    # Check if there are consecutive zeros at the end of the list
    if count > 0:
        end_index = len(lst) - 1
        result.append({'count': count, 'starting_index': start_index, 'ending_index': end_index})

    return result

lst = [1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0]
output = find_consecutive_zeros(lst)
print(output)
