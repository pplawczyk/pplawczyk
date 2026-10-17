import subprocess
from check_data import check_data_folder, check_data_file

subprocess.run("cls", shell=True, check=True)
print("Info: Program started.")

check_data_folder()
check_data_file()

print("Info: Program edned.")
