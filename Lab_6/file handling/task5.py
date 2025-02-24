def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.writelines("\n".join(data))


my_list = list(map(str, input().split()))
write_list_to_file(r"C:\Users\Artemida\Desktop\Аида\PP2\Lab_6\file handling\example.txt", my_list)
