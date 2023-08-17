"""
Python Program for Replace All 0’s With 1 In A Given Integer

Implementation
We will convert the integer into string.
Then we will convert it into list and then we will traverse through the list.
Wherever we find a ‘0’ we will replace with ‘1’.


Algorithm
Take Input in num and initialize a variable num with with value 0
If num is equals to zero then update the value of num2 to 1
Iterate using a while loop until num is greater then 0
For each iteration initialize a variable rem and store unit digit of num
If rem equals to 0 then set rem to 1
Set num to num divide by 10 & num2 equals to num2*10+rem
Reverse and print num2

"""


# Method 1
num = int(input("Enter number : "))
num2 = 0

if num == 0:
    num2 = 1

while num > 0:
    rem = num % 10
    if rem == 0:
        rem = 1
    num = num//10
    num2 = num2 * 10 + rem

num = 0
while num2 > 0:
    r = num2 % 10
    num = num * 10 + r
    num2 //= 10

print("Converted number is:", num)


# Method 2
Val = int(input('Enter number:'))
Val = str(Val)      # change type to string
Replaced = Val.replace('0', '1')
print(Replaced)
