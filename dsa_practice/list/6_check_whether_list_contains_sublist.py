
"""
32. Write a Python program to check whether a list contains a sublist.

"""
test_list = [5, 6, 3, 8, 2, 1, 7, 1]

sublist = [8, 2, 7]

# Check for Sublist in List
c = 0
res = False
for i in sublist:
    if i in test_list:
        c += 1
if(c == len(sublist)):
    res = True

print(res)


def isSublist(list_, sublist):
    if not isinstance(list_, list):
        list_ = list(list_)
    sublen = len(sublist)
    for i in range(len(list_)-sublen+1):
        if list_[i:i+sublen] == sublist:
            return True
    return False


list_ = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(isSublist(list_, [0, 1]))  # --> True
