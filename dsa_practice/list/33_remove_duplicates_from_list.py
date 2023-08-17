
"""

7. Write a Python program to remove duplicates from a list. 

"""

lst = [3,4,5,7,3,2,4,2,2]

res = []


for n, i in enumerate(lst):
  if i not in lst[:n]:
    res.append(i)
    
    

# for i in lst:
#   if i not in res:
#     res.append(i)


res = [lst[i] for i in range(len(lst)) if i == lst.index(lst[i]) ]


# using numpy
res = np.unique(lst)
    
print(res)
