import math
def poly(n, a):
    return (n*(a**2)/(4*math.tan(math.pi/n)))

side=int(input())
a1=int(input())
print(int(poly(side, a1)))