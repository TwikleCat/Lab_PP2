import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 10, 17, 19, 22, 29]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)