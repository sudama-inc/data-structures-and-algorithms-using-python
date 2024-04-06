# List: 30

# # You have a list containing 0 and 1. Remove all consecutive 1 from the list.
# # input: 0,0,1,1,1,0,1,0,1,1,0
# # output: 0,0,1,0,1,0,1,0

# lst = [1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0]
# op = []
# for i in lst:
#     if not len(op):
#         op.append(i)
#     elif i != op[-1]:
#         op.append(i)
#     elif i == 0:
#         op.append(i)

# print(op)



# import random as re
#
#
# # Generate 10 random integers between 1 and 10 (inclusive)
# random_integers = re.sample(range(1, 11), 10)
#
# print(random_integers)