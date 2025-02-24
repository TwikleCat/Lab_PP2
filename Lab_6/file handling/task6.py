import string, os

if not os.path.exists(r"c:\Users\Artemida\Desktop\Аида\PP2\Lab_6\file handling\letters"):
   os.makedirs(r"c:\Users\Artemida\Desktop\Аида\PP2\Lab_6\file handling\letters")

for letter in string.ascii_uppercase:
    file_path = os.path.join(r"c:\Users\Artemida\Desktop\Аида\PP2\Lab_6\file handling\letters", f"{letter}.txt")  
    with open(file_path, "w") as f:
        f.write(letter)


