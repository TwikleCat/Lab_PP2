def divis(n):
    for nim in range(n+1):
        if nim%3==0 and nim%4==0:
            yield nim

num=int(input())
print(list(divis(num)))
