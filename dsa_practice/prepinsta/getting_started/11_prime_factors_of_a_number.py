"""
Python program that calculates the prime factors of a given number using loops:

"""


def get_prime_factors(number):
    prime_factors = []
    
    # Handle the case where the number is less than 2
    if number < 2:
        return "Prime factors are not defined for numbers less than 2."

    # Find and append the prime factors
    for i in range(2, int(number**0.5) + 1):
        while number % i == 0:
            prime_factors.append(i)
            number //= i

    return prime_factors

# Example usage:
input_number = 100  # Change this to the desired number
result = get_prime_factors(input_number)
print(f"The prime factors of {input_number} are: {result}")