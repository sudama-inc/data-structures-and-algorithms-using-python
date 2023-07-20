"""
***
74. Write a Python program to find the minimum window in a given string that will
contain all the characters of another given string.

Input : str1 = " PRWSOERIUSFK "
str2 = " OSU "
Output: Minimum window is "OERIUS"

https://www.geeksforgeeks.org/python-get-the-smallest-window-in-a-string-containing-all-characters-of-given-pattern/
https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/


75. Write a Python program to find the smallest window that contains all characters in a given string.

"""

# Method 1
import collections


def smallestWindow(s, p):
    n = len(s)
    if n < len(p):
        return -1
    mp = [0]*256

    # Starting index of ans
    start = 0
    ans = n + 1
    cnt = 0

    # creating map
    for i in p:
        mp[ord(i)] += 1
        if mp[ord(i)] == 1:
            cnt += 1

    j = 0
    i = 0

    # Traversing the window
    while(j < n):

        # Calculating
        mp[ord(s[j])] -= 1
        if mp[ord(s[j])] == 0:
            cnt -= 1

            # Condition matching
            while cnt == 0:
                if ans > j - i + 1:
                    # calculating answer.
                    ans = j - i + 1
                    start = i
                # Sliding I Calculation for removing I
                mp[ord(s[i])] += 1
                if mp[ord(s[i])] > 0:
                    cnt += 1
                i += 1
        j += 1
    if ans > n:
        return "-1"
    return s[start:start+ans]


# Driver code
if __name__ == "__main__":
    s = "this is a test string"
    p = "tist"
    result = smallestWindow(s, p)
    print(result)


# Method 2


def min_window(str1, str2):
    result_char, missing_char = collections.Counter(str2), len(str2)
    i = p = q = 0
    for j, c in enumerate(str1, 1):
        missing_char -= result_char[c] > 0
        result_char[c] -= 1
        if not missing_char:
            while i < q and result_char[str1[i]] < 0:
                result_char[str1[i]] += 1
                i += 1
            if not q or j - i <= q - p:
                p, q = i, j
    return str1[p:q]


str1 = "PRWSOERIUSFK"
str2 = "OSU"
print(min_window(str1, str2))
