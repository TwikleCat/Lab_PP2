import os
path=r'C:\Users\Artemida\Desktop\Аида\Enterprise Architecture\Assignment 2.docx'
print('Exist:', os.access(path, os.F_OK))
print('Readable:', os.access(path, os.R_OK))
print('Writable:', os.access(path, os.W_OK))
print('Executable:', os.access(path, os.X_OK))
