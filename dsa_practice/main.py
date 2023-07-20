

# # You have a list containing 0 and 1. Remove all consecutive 1 from the list.
# # input: 0,0,1,1,1,0,1,0,1,1,0
# # output: 0,0,1,0,1,0,1,0

# # op = [0,0,1,0]


# lst = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0]
# # input: 0,0,1,1,1,0,1,0,1,1,0
# # output: 0,0,1,0,1,0,1,0
# # res = []
# # for i in range(len(lst)-1):
# #     if lst[i] == 0:
# #         res.append(lst[i])
# #     if lst[i] == 1:
# #         if lst[i] == lst[i+1]:
# #             res.append(lst[i])

# # print(res)
# res = []

# for i in range(len(lst)-1):
#     if lst[i] == 0:
#         res.append(lst[i])

#     else:
#         if res[-1] != 1:
#             res.append(lst[i])

# if lst[-1] == 0:
#     res.append(lst[-1])

# else:
#     if res[-1] != 1:
#         res.append(lst[-1])


# print(res)


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


# Check Palindrome
n = 21123
temp = n
res = 0
while (n != 0):
    res = ((res*10) + (n % 10))
    n = n//10

if temp == res:
    print('palindrome')
else:
    print('not palindrome')
