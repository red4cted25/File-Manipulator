# File Manipulator

The objective of this assignment is to practice and demonstrate proficiency in handling files and folders through a series of tasks involving common file operations, folder manipulations, and file manipulations.



## File Operations

| Task                                 | Function |
| :----------------------------------- | :------- |
| Create a text file named sample.txt  | `def write_file(file_path, text_to_write)` |
| Read the content of sample.txt       | `def read_file(file_path)` |
| Append additional text to sample.txt | `def append_file(file_path, text_to_write)` |

#### Create a text file named sample.txt
This function writes the specified text to a file at the given file path.
```bash
  def write_file(file_path, text_to_write):
    with open(file_path, 'w') as file:
        file.write(text_to_write)
    print(f'"{text_to_write}" written!')
```

#### Read the content of sample.txt    
This function reads the content of a file at the specified file path.
```bash
  def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return content
```

#### Append additional text to sample.txt
This function appends the specified text to the end of a file.
```bash
  def append_file(file_path, text_to_write):
    with open(file_path, 'a') as file:
        file.write(text_to_write)
    print(f'"{text_to_write}" appended!')
```

## Folder Manipulation

| Task                                  | Function |
| :------------------------------------ | :------- |
| Create a folder named Files           | `def make_directory(path)` |
| Move sample.txt into the Files folder | `def move(starting_path, ending_path)` |

#### Create a folder named Files 
This function creates a new directory at the specified path.
```bash
  def make_directory(path):
    os.mkdir(path)
    print("Directory created!")
```

#### Move sample.txt into the Files folder    
This function moves a file from the starting path to the ending path.
```bash
  def move(starting_path, ending_path):
    shutil.move(starting_path, ending_path)
    print(f'"{starting_path}" moved!')
```


## File Manipulation

| Task                                 | Function |
| :----------------------------------- | :------- |
|  Create two additional text files: file1.txt and file2.txt  | `def write_file(file_path, text_to_write)` |
| Rename file1.txt to renamed_file.txt       | `def rename_file(starting_path, ending_path)` |
| Delete file2.txt | `def remove(path)` |

#### Create two additional text files: file1.txt and file2.txt
This function writes the specified text to a file at the given file path.
```bash
  def write_file(file_path, text_to_write):
    with open(file_path, 'w') as file:
        file.write(text_to_write)
    print(f'"{text_to_write}" written!')
```

#### Rename file1.txt to renamed_file.txt    
This function renames a file from the starting path to the ending path.
```bash
  def rename_file(starting_path, ending_path):
    os.rename(starting_path, ending_path)
    print(f'"{starting_path} renamed!') 
```

#### Delete file2.txt
This function removes a file at the specified path.
```bash
  def remove(path):
    os.remove(path)
    print(f'"{path}" removed!')
```

## Additional Operations

| Task                                 | Function |
| :----------------------------------- | :------- |
| List all the files in the Files folder  | `def find_files_and_folders(path)` |
| Zip the entire Files folder into a compressed file named archive.zip       | `def zip(name, type, path)` |


#### List all the files in the Files folder
This function recursively lists all files and folders in a directory.
```bash
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
```

#### Zip the entire Files folder into a compressed file named archive.zip   
This function creates a zip archive of a directory.
```bash
  def zip(name, type, path):
    shutil.make_archive(name, type, path)
    print(f'"{path}" was zipped as {name}!')
```


## Authors

- [@red4cted25](https://www.github.com/red4cted25)
