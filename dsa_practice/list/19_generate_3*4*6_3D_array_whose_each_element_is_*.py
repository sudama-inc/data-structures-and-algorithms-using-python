
"""

13. Write a Python program to generate a 3*4*6 3D array whose each element is *. 

"""

from pprint import pprint
array = [[['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)


list_1 = [[['*']*6 for col in range(4)] for row in range(3)]
pprint(list_1)
