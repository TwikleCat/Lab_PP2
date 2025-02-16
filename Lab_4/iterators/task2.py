def even(n):
     return(i for i in range(n+1) if i % 2 == 0)
num=10
for n in even(num):
     print(n, end=", ")
       