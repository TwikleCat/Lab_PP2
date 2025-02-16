def square_number(n):
    for x in range (n+1):
        yield x**2

n=14
for num in square_number(n):
    print(num)