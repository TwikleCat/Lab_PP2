import re
def task6(str):
    word=re.sub('[ ,.]', ':', str)
    return word

inp=input()
print(task6(inp))