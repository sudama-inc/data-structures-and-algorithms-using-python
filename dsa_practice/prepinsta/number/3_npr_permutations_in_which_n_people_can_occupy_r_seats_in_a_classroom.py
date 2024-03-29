"""
Python Program for Permutations In Which N People Can Occupy R Seats In A Classroom
Which n people can occupy r seats in a classroom in Python

Here, we will discuss program for Permutations In Which N People Can
Occupy R Seats in python .In this python program, we will be defining the
number of ways in which N number of students can occupy R number of seats. 
Take an example Ten friends enter the classroom late and all the seats are 
occupied by toppers of the college and now only Six seats are available so 
in how many ways are those Ten friends will occupy Six seats although 4 students
have to leave the classroom. We will use math library for factorial function in 
building of this program.

"""

"""
Algorithm
Input number of students in n
Input number of seats in r
Use permutation formula { factorial(n) / factorial(n-r) }
Print Output
"""


def factorial(num):
    fact = 1
    for i in range(num, 1, -1):
        fact *= i
    return fact


# main program
# user input
n = int(input("Enter number of people: "))
r = int(input("Enter number of seats: "))

# finding all possible arrangements of n people on r seats
# by using formula of permutation
p = factorial(n) // factorial(n - r)

# printing output
print("Total possible arrangements:", p)
