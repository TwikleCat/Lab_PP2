def task2(str):
    u=sum(1 for i in str if i.isupper())
    l=sum(1 for i in str if i.islower())
    return u, l

s=input()
print(task2(s))