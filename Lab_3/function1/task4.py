def filter_prime(numbers):
    primes = []
    for num in numbers:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
prime_numbers = filter_prime(numbers)
print(prime_numbers)
