# Na początku sprawdzam czy istnieje katalog z danymi
from check_data import check_folders, check_data_file

print("Info: Program started.")

if check_folders() == False:
        print("Checking: Error: Missing folder with data.")
else:
        print("Checking: Passed: Folder with data exists")

if check_data_file() == False:
        print("Checking: Error: Missing JSON data file.")
else:
        print("Checking: Passed: JSON file with data exists")


print("Info: Program edned.")
