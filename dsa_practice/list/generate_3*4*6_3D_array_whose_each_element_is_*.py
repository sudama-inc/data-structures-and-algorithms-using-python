
"""

13. Write a Python program to generate a 3*4*6 3D array whose each element is *. 

"""

array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)


from pprint import pprint
list_1 = [[[col*row]*6 for col in range(4)] for row in range(3)]
pprint(list_1)
