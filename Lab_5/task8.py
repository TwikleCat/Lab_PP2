import re
input=input()
print(re.findall('[A-Z][^A-Z]*', input))
