from functools import reduce

def mult(x, y):
    return x * y

a=[2, 3, 4, 5]
result=reduce(mult, a)
print(result)

inp=list(map(int, input().split()))
result2=reduce(lambda x, y: x*y, inp)
print(result2)


