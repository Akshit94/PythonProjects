import os
import string

def rename_files():
    # (1) get the directory where the files are stored
    # here 'r' stands for "raw pack" which tells the listdir() that
    # treat this string as it is.
    files_path = os.listdir(r"C:\PythonProjects\alphabet")
    print(files_path)
    # cwd = CurrentWorkingDirectory
    saved_path = os.getcwd()
    # os.chdir() is used to change the directory
    os.chdir(r"C:\PythonProjects\alphabet")
    # (2) rename the files in the directory
    for file_name in files_path:
        os.rename(file_name, string.translate(file_name, None, "0123456789"))
    os.chdir(saved_path)
    
rename_files()
