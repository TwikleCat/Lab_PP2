def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        dest.write(src.read())


copy_file(r"C:\Users\Artemida\Desktop\Аида\PP2\Lab_6\file handling\letters\A.txt", r"C:\Users\Artemida\Desktop\Аида\PP2\Lab_6\file handling\letters\B.txt")
