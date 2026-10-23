# Tutaj utworzę sobie fukcje, którymi będę sprawdzał różne rzeczy przed uruchomieniem całego rozwiązania.
# Na początek sprawdzę czy mam dostęp do pliku JSON z paragonami

from pathlib import Path        # pathlib to standartowa bibliotego pythona używana do pracy ze ścieżkami katalogów
import uuid                     # do obsługi formatów UUID
import ijson                    # do obsługi danych w json w formie całych elementów 
from datetime import datetime   # do obługi formatów daty 

# sprawdź czy istnieje folder z danymi
def check_data_folder():
    # Zmienna, której przypisuje folder w którym znajduje się JSON z paragonami 
    data_folder = Path.cwd() / "data"
    if data_folder.is_dir():
        print("Checking: Passed: Data folder exists.\n")
        return True
    else:
        print("Checking: Error: Missing folder with data.\n")
        return False

# sprawdź czy w folderrze znajduje się niepusty plik 
def check_data_file():
    my_file = Path.cwd() / "data/receipts.json"
    if not my_file.is_file():
        print("Checking: Error: JSON file doesn't exist.\n")
        return False
    elif my_file.stat().st_size == 0:
        print("Checking: Error: JSON file has 0 size.\n")
        return False
    else:
        print("Checking: Passed: JSON file is not empty.\n")
        return True

# sprawdź czy ciąg znaków jest zgodny z UUID, do tego potrzebna mi biblioteka uuid
def check_uuid(value):
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False

# sprawdź ile argumentów wywołano
def check_arguments_no(arguments) -> bool:
# # dla sprawdzenia wypiszę argumenty, które podano
#     print(f"*"*60)
#     print(f"Liczba podanych argumentów to: {len(arguments)}")
#     for argument_name in arguments:
#         values = arguments.getlist(argument_name)
#         for value in values:
#             print(f"Nazwa argumentu: {argument_name}, wartość: {value}")
#     print(f"*"*60)
    if len(arguments) in (1,2):
        print("Checking: Passed. Good number of arguments. 1 or 2. \n")
        return True
    else:
        print("Checking: Error. Wrong number of arguments.\n")
        return False

# sprawdź czy podany str jest w formacie daty: rrrr-mm-dd
def check_if_date(date_string: str) -> bool:
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        print(f"Checking: Passed: String \"{date_string}\" looks like correct date format.\n")
        return True
    
    except ValueError:
        print("Checking: Error: This argument doesn't look like correct date.\n")
        return False

# Tu są rzeczy już nie potrzebne
# Sprawdź czy wywołany argument jest o właściwej nazwie
def check_arguments_name(arguments, name: str) -> bool:
    if name in arguments:
        print(f"Checking: Passed: Arument name is: {name}.\n")
        return True
    else:
        print(f"Checking: Error. Wrong argument name: {name}.\n")
        return False