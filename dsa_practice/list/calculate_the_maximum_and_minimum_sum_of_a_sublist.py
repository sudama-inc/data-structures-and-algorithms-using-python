"""
***
182. Write a Python program to calculate the maximum and minimum sum
of a sublist in a given list of lists.
 
Original list: [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
Maximum sum of sub list of the said list of lists: [2, 3, 5, 4]
Minimum sum of sub list of the said list of lists: [1, 2, 1, 2]

https://stackoverflow.com/questions/15062844/maximum-sum-sublist
https://www.geeksforgeeks.org/python-maximum-sum-sublist/
https://www.geeksforgeeks.org/python-maximum-sum-elements-list-list-lists/
"""


# Method 1
def mssl(l):
    best = cur = l[0]
    for i in range(len(l)):
        cur = max(cur + l[i], l[i])
        best = max(best, cur)
    return best


print(mssl([-6, -44, -5, -4, -9, -11, -3, -99]))


# # Method 2
def mssl(l):
    best = cur = 0
    curi = starti = besti = 0
    for ind, i in enumerate(l):
        if cur+i > 0:
            cur += i
        else:  # reset start position
            cur, curi = 0, ind+1

        if cur > best:
            starti, besti, best = curi, ind+1, cur
    return starti, besti, best


# Method 3
# By DP Approach
test_matrix = [[1, 3, 1], [4, 5, 3], [1, 2, 4]]

# using dynamic programming maximum sum sublist
dp = test_matrix[0]
max_sum = sum(dp)
max_row = 0

for i in range(1, len(test_matrix)):
    for j in range(len(test_matrix[0])):
        if j == 0:
            dp[j] = test_matrix[i][j]
        else:
            dp[j] = max(dp[j-1], 0) + test_matrix[i][j]
        if dp[j] > max_sum:
            max_sum = dp[j]
            max_row = i

res = test_matrix[max_row]

# printing result
print(res)
