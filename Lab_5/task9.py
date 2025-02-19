import re
def task9(str):
    return re.sub("(\w)([A-Z])", r"\1 \2", str)

print(task9("HelloWorld"))  
print(task9("camelCaseExample")) 
