"""
write a python code to apply zero padding on the list please do not use any predefine library.
add - Pre Padding
add - Post Padding

"""

def zero_padding(input_list):
    max_length = max(len(sublist) for sublist in input_list)
    
    padded_list = []
    for sublist in input_list:
        padding = [0] * (max_length - len(sublist))
        padded_sublist = sublist + padding  # Post Padding
        # padded_sublist = padding + sublist # Pre Padding
        padded_list.append(padded_sublist)
    
    return padded_list

# Example usage:
input_list = [[1, 2], [3, 4, 5, 7, 8, 4, 3, 2, 5], [1, 2, 4, 5, 6], [5, 7, 5]]
result_list = zero_padding(input_list)

print(result_list)