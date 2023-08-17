"""
****
6. Write a Python program to get a list, sorted in increasing order by the 
last element in each tuple from a given list of non-empty tuples.

Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-tuples-in-increasing-order-by-the-last-element-in-each-tuple/


"""
# Method 1: Using Bubble Sort.

def Sort_Tuple(tup):
	lst = len(tup)
	for i in range(0, lst):
		
		for j in range(0, lst-i-1):
			if (tup[j][-1] > tup[j + 1][-1]):
				temp = tup[j]
				tup[j]= tup[j + 1]
				tup[j + 1]= temp
	return tup

# Driver Code
tup =[(1, 3), (3, 2), (2, 1)]
		
print(Sort_Tuple(tup))



# Method 2: Using Insertion Sort.

def Sort_Tuple(tup):
	n = len(tup)
	for i in range(1, n):
		key = tup[i]
		j = i - 1
		while j >= 0 and key[1] < tup[j][1]:
			tup[j + 1] = tup[j]
			j -= 1
		tup[j + 1] = key
	return tup

# Driver Code
tup = [(1, 3), (3, 2), (2, 1)]

# printing the sorted list of tuples
print(Sort_Tuple(tup))




#Method 3: Using Merge Sort
def merge_sort(lst):
	if len(lst) <= 1:
		return lst
	mid = len(lst) // 2
	left = lst[:mid]
	right = lst[mid:]
	left = merge_sort(left)
	right = merge_sort(right)
	return merge(left, right)

def merge(left, right):
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i][1] <= right[j][1]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while i < len(left):
		result.append(left[i])
		i += 1
	while j < len(right):
		result.append(right[j])
		j += 1
	return result

def Sort_Tuple(tup):
	return merge_sort(tup)

# Driver Code
tup = [(1, 3), (3, 2), (2, 1)]

# printing the sorted list of tuples
print(Sort_Tuple(tup))


