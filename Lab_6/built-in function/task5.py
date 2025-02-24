def task5(list):
    return all(list)

my_list=list(map(int, input().split()))
lis=[False, True, False, True]
print(task5(my_list))
print(task5(lis))