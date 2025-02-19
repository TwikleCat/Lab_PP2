import re
def task10(str):
    word=re.sub(r"(\w)([A-Z])", r"\1_\2", str)
    words=word.lower()
    return words
    

print(task10("HelloWorldTest"))
