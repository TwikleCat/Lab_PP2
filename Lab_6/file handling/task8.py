import os

def task8(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
    else:
        print("Do not exist or access denied.")

task8(r"C:\Users\Artemida\Desktop\Аида\PP2\Lab_6\file handling\ex.txt")
