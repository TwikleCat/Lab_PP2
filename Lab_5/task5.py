import re
def task5(str):
    pattern='a.*b$'
    if re.search(pattern, str):
        return "Found a match!"
    else: 
        return "None"

inp=input()
print(task5(inp))
