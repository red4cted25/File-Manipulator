import shutil, os

def write_file(file_path, text_to_write):
    with open(file_path, 'w') as file:
        file.write(text_to_write)
    print(f'"{text_to_write}" written!')
    
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return content

def append_file(file_path, text_to_write):
    with open(file_path, 'a') as file:
        file.write(text_to_write)
    print(f'"{text_to_write}" appended!')

def make_directory(path):
    os.mkdir(path)
    print("Directory created!")

def move(starting_path, ending_path):
    shutil.move(starting_path, ending_path)
    print(f'"{starting_path}" moved!')

def rename_file(starting_path, ending_path):
    os.rename(starting_path, ending_path)
    print(f'"{starting_path} renamed!') 

def remove(path):
    os.remove(path)
    print(f'"{path}" removed!')

def zip(name, type, path):
    shutil.make_archive(name, type, path)
    print(f'"{path}" was zipped as {name}!')

def find_files_and_folders(path):
    for root, dir, files in os.walk(path):
        print(f"Current directory: {root}")
        print("Directories:")
        for directory in dir:
            print(os.path.join(root, directory))
        print("Files:")
        for file in files:
            print(os.path.join(root, file))
        print("--------------------------------------")

# FILE OPERATIONS:
write_file("C:/Users/ndiaz413/Desktop/Yr. 1 VS Code\Python\File Manipulation\Assignment\sample.txt")
read_file("C:/Users/ndiaz413/Desktop/Yr. 1 VS Code\Python\File Manipulation\Assignment\sample.txt")
append_file("C:/Users/ndiaz413/Desktop/Yr. 1 VS Code\Python\File Manipulation\Assignment\sample.txt", "\nAdditional line added for file operations.")

# FOLDER MANIPULATION
make_directory("C:/Users/ndiaz413/Desktop/Yr. 1 VS Code\Python\File Manipulation\Assignment\The Cool Zone")
move('C:/Users/ndiaz413/Desktop/Yr. 1 VS Code\Python\File Manipulation\Assignment\sample.txt', 'C:/Users/ndiaz413/Desktop/Yr. 1 VS Code\Python\File Manipulation\Assignment\Files')

# FILE MANIPULATION
write_file("C:/Users/ndiaz413/Desktop/Yr. 1 VS Code\Python\File Manipulation\Assignment\Files/file1.txt", "the coolest kind of beans")
write_file("C:/Users/ndiaz413/Desktop/Yr. 1 VS Code\Python\File Manipulation\Assignment\Files/file2.txt", "there can only be one beans.")
rename_file("C:/Users/ndiaz413/Desktop/Yr. 1 VS Code\Python\File Manipulation\Assignment\Files/file1.txt", "C:/Users/ndiaz413/Desktop/Yr. 1 VS Code\Python\File Manipulation\Assignment\Files/renamed_file.txt")
remove("C:/Users/ndiaz413/Desktop/Yr. 1 VS Code\Python\File Manipulation\Assignment\Files/file2.txt")

# ADDITIONAL OPERATIONS
find_files_and_folders("C:/Users/ndiaz413/Desktop/Yr. 1 VS Code\Python\File Manipulation\Assignment\Files")
zip('archive', 'zip', 'C:/Users/ndiaz413/Desktop/Yr. 1 VS Code\Python\File Manipulation\Assignment\Files')
