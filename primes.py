"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes must be positive")

    prime_list = []
    number = 2
    while len(prime_list) < number_of_primes:
        if is_prime(number):
            prime_list.append(number)
        number += 1
    return prime_list
