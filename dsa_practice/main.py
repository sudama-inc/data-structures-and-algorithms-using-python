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


# Check Palindrome
# n = 21123
# temp = n
# res = 0
# while (n != 0):
#     res = ((res*10) + (n % 10))
#     n = n//10

# if temp == res:
#     print('palindrome')
# else:
#     print('not palindrome')


# num = 1214
# temp = num
# sum = 0
# while num > 0:
#     sum += num % 10
#     num = num // 10
# print(sum)
