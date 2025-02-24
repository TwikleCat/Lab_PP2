
import os, string
for letter in string.ascii_uppercase:
     file_path = os.path.join(r"c:\Users\Artemida\Desktop\Аида\PP2\Lab_6\file handling\letters", f"{letter}.txt")
     os.remove(file_path)

