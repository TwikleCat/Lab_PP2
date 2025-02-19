import re
def task2(str):
    return bool(re.search('ab{2,3}', str))


strin=input()
print(task2(strin))