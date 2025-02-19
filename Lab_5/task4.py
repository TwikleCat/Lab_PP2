import re
def task4(str):
    return bool(re.search('[A-Z][a-z]+', str))

inp=input()
print(task4(inp))
