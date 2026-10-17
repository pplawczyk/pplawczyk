import subprocess
from check_data import check_data_folder, check_data_file
from webservice import webservice_start

subprocess.run("cls", shell=True, check=True)
print("Info: Program started.")

check_data_folder()
check_data_file()
webservice_start()


print("Info: Program edned.")
