"""
***
Reverse an Array using Python
Here, in this page we will discuss the program to reverse an array using
python programming language. We will discuss different approaches to reverse
the array in this page and compare the complexity of different approaches.


Example :
Let's array is arr[5] = [10, 20, 30, 40, 50] n = 5
i = 0, j = 4
As (0 is less than 4) swap(arr[0],arr[4])
arr[0]=50 and arr[4]=10, i++(i.,e i=1) and j--(i.e, j=3)
Again (1 is less than 3) swap(arr[1],arr[3])
arr[1]=40 and arr[3]=20, i++(i.,e i=2) and j--(i.e, j=2)
Now, i is not less than j (as i=2 and j=2) so loop gets terminate and
original array get reversed.

"""

"""
***
Method 1 : Using Swapping
Take two variables say start = 0 and end= arr.len()-1
Run a loop till start < end
Swap arr[start] with arr[end]
Increment start and decrement end by 1
Print array
"""


def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1


A = [10, 20, 30, 40, 50]
reverseList(A, 0, 4)
print(A)


"""
Method 2 : Using Recursion
Create a recursive function reverseList and pass array , start and end index of array.
Recursively call the function reverseList.
"""


def reverseList(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverseList(arr, start+1, end-1)


# Driver function to test above function
A = [10, 20, 30, 40, 50]
reverseList(A, 0, 4)
print(A)


# Method 3 : Reverse the array using list slicing
def reverseList(A):
    print(A[::-1])


# Driver function to test above function
A = [10, 20, 30, 40, 50]
reverseList(A)


# Method 4 : using For Loop with Reverse Iteration
res = [A[i] for i in range(len(A)-1, -1, -1)]
print(res)
