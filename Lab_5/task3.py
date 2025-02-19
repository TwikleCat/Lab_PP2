import re 
def task3(str):
    pattern='[a-z]+_[a-z]+'
    if re.findall(pattern, str):
        return "Found a match!"
    else:
        return "None"
    

strin=input()
print(task3(strin))