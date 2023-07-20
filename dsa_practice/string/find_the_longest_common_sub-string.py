"""
***
69. Write a Python program to find the longest common sub-string from two given strings.

https://www.geeksforgeeks.org/longest-common-substring-dp-29/
"""


# Method 1
def LCSubStr(X, Y, m, n):
    # Create a table to store lengths of longest common suffixes of substrings.
    # Note that LCSuff[i][j] contains the length of longest common suffix of
    # X[0...i-1] and Y[0...j-1].
    # LCSuff is the table with zero value initially in each cell
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]

    # To store the length of longest common substring
    result = 0

    # Following steps to build LCSuff[m+1][n+1] in bottom up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i-1] == Y[j-1]):
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return result


# Driver Code
X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'
m = len(X)
n = len(Y)

print(LCSubStr(X, Y, m, n))


# Method 2
def lcs(i, j, count):
    if (i == 0 or j == 0):
        return count

    if (X[i - 1] == Y[j - 1]):
        count = lcs(i - 1, j - 1, count + 1)

    count = max(count, max(lcs(i, j - 1, 0),
                           lcs(i - 1, j, 0)))

    return count


# Driver code
if __name__ == "__main__":

    X = "abcdxyz"
    Y = "xyzabcd"
    n = len(X)
    m = len(Y)

    print(lcs(n, m, 0))
