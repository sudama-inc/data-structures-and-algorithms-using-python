"""
Leap Year Program in Python : Leap-year-or-not-using-python
Check if a Year is a Leap Year or Not in Python
Given an integer input year, the objective of the code is to Check if a Year is a Leap Year or Not in Python Language. To do so  we’ll check if the year input satisfies either of the two conditions of leap year.

Example
Input : 2020
Output : It's a Leap Year.


Conditions for a Leap Year : 
Here are the two conditions that any year must satisfy to be called a leap year
1. The year must be perfectly divisible by 400.
2. The number must be divisible by 4 but not by 100.
"""

# Method 1: Using if-else Statements 1
year = 2000
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
