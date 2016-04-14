import math

def is_prime(n):
    # Check to make sure number isn't even and isn't less than 2.
    if n % 2 == 0 and n > 2:
        return False
    # Check to see if every odd number from 3 to one greater than
    # the square root of n evenly divide into n. If any of them
    # do so, return False. Otherwise, return True.
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def get_how_many_prime_numbers(n):
    i = 2
    results = []
    while True:
        if is_prime(i):
            results.append(i)
        if len(results) >= n:
            return results
        i += 1
