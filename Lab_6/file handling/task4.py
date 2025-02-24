
with open(r"C:\Users\Artemida\Desktop\Аида\PP2\Lab_6\file handling\example.txt", 'r') as fp:

	lines = len(fp.readlines())
	print(lines)

def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print(file_lengthy(r"C:\Users\Artemida\Desktop\Аида\PP2\Lab_6\file handling\example.txt"))