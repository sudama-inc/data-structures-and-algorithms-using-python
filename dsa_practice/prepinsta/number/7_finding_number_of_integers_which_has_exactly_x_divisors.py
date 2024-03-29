"""
Python program to find number of integers which has exactly x divisors.

program that count the number of integers which has exactly x divisors in python.
Numbers dividing with self or 1 are called prime numbers but numbers having
multiple divisors are called composite numbers.

"""

"""
Method 1 :
Declare a variable count =0, to count the required numbers with x factors.
Run a loop for range 1 to n.
Inside that take a variable count_factors = 0, that will count the factors of ith.
Now, run a inner loop.
And increase the count_factors if it’s is factor of ith number.
Check if count_factors == X, then increment the count by 1.
At last print the count value.
"""
import math
Number = 7
Divisor = 2
# count is to count total number of Numbers with exact divisor
count = 0
# driver loop
for i in range(1, Number+1):
    # count_factors checks the total number of divisors
    count_factors = 0
    # loop to find number of divisors
    for j in range(1, i+1):
        if i % j == 0:
            count_factors += 1
        else:
            pass
    if count_factors == Divisor:
        count += 1

# for break in line between Numbers and total count
print(count)


"""
Method 2 : In this method we will use the efficient way for counting the factors
that used in method 1. We use the sieve of eratosthenes for counting the factors.
"""


def sieve(primes, x):
    primes[1] = False

    i = 2
    while (i * i <= x):
        if (primes[i] == True):
            j = 2
            while (j * i <= x):
                primes[i * j] = False
                j += 1
        i += 1


def nDivisors(primes, x, a, b, n):

    result = 0

    v = []
    for i in range(2, x + 1):
        if (primes[i]):
            v.append(i)

    for i in range(a, b + 1):

        temp = i

        total = 1
        j = 0

        k = v[j]
        while (k * k <= temp):

            count = 0

            while (temp % k == 0):
                count += 1
                temp = int(temp / k)

            total = total * (count + 1)
            j += 1
            k = v[j]

        if (temp != 1):
            total = total * 2

        if (total == n):
            result += 1
    return result


def countNDivisors(a, b, n):
    x = int(math.sqrt(b) + 1)

    primes = [True] * (x + 1)
    sieve(primes, x)

    return nDivisors(primes, x, a, b, n)


n = 7
x = 2
print(countNDivisors(1, n, x))
