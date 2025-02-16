def squares(a, b):
    for i in range(a, b+1):
        yield i**2

c=int(input())
d=int(input())
print(list(squares(c, d)))