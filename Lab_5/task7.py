import re 
def task7(str):
    word=str.split('_')
    result=word[0]+''.join(x.capitalize() for x in word[1:])
    return result

inp=input()
print(task7(inp))
    