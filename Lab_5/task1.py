import re
def task_1(str):
    pattern='ab*'
    if re.search(pattern, str):
        return "Found a match!"
    else:
        return "None"

strin="dsfgffeu"
print(task_1(strin))