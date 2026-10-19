# Tutaj utworzę sobie fukcje, którymi będę sprawdzał różne rzeczy przed uruchomieniem całego rozwiązania.
# Na początek sprawdzę czy mam dostęp do pliku JSON z paragonami

# pathlib to standartowa bibliotego pythona używana do pracy ze ścieżkami,
from pathlib import Path
import uuid
import ijson

def check_data_folder():
    # Zmienna, której przypisuje folder w którym znajduje się JSON z paragonami 
    data_folder = Path.cwd() / "data"
    if data_folder.is_dir():
        print("Checking: Passed: data folder exists.")
        return True
    else:
        print("Checking: Error: Missing folder with data.")
        return False

def check_data_file():
    my_file = Path.cwd() / "data/receipts.json"
    if not my_file.is_file():
        print("Checking: Error: JSON file doesn't exist.")
        return False
    elif my_file.stat().st_size == 0:
        print("Checking: Error: JSON file has 0 size.")
        return False
    else:
        print("Checking: Passed: JSON file is not empty.")
        return True


# sprawdzam czy wywołano wałaściwe argumenty
def check_arguments(arguments, number_of_args: int) -> bool:
    for argument_name in arguments:
        values = arguments.getlist(argument_name)
        for value in values:
            print(f"Nazwa argumentu: {argument_name}, wartość: {value}")
    return True











# sprawdzam czy receiptId ma format zgodny z UUID, do tego potrzebna mi biblioteka uuid
def check_receiptId(receiptId):
    try:
        uuid.UUID(receiptId)
        print("Podana wartość jest zgodna z UUID.")
        return True
    except ValueError:
        print("Podana wartość nie jest zgodna z UUID.")
        return False

