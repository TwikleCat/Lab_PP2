def rever(n):
    while n>=0:
        yield n
        n-=1

num=10
print(list(rever(num)))