# Tutaj utworzę sobie fukcje, którymi będę sprawdzał różne rzeczy przed uruchomieniem całego rozwiązania.
# Na początek sprawdzę czy mam dostęp do pliku JSON z paragonami

# pathlib to standartowa bibliotego pythona używana do pracy ze ścieżkami,
from pathlib import Path
import uuid
import ijson

# w tej funkcji sprawdzam czy w pliku z pragaonami znajduje się paragon o podanym UUID i jeśli go znajdę to zwrócę jego zawartość
def get_receipt(receipt_id):
        # Sprawdzam czy w wyołaniu funkcji id paragonu jest w formacie UUID 
        if not check_uuid(receipt_id):
            print("Checking: Error: Value is not in UUID format.\n")
            return False
        print("Checking: Passed. ReceiptId looks like UUID.\n")

        # Ustalam ścieżkę do pliku danych
        file_path = Path(__file__).resolve().parent / "data" / "receipts.json"
        print(f"Info: Path to JSON with data is: {file_path}\n")

        # Przy użyciu otwartego pliku...
        with open(file_path, "rb") as file:

            # Sprawdzam kolejne elementy JSON-a
            for receipt in ijson.items(file, "receipts.item"):
                saved_receipt_id = receipt.get("document", {}).get("receiptId")
                print(f"Sprawdzam element: {saved_receipt_id}")
                if saved_receipt_id == receipt_id:
                    print(f"Znaleziony element to: {saved_receipt_id}")
                    return True

        return False












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


















# Niepotrzebne. Sprawdź czy wywołany argument jest o właściwej nazwie
def check_arguments_name(arguments, name: str) -> bool:
    if name in arguments:
        print(f"Checking: Passed: Arument name is: {name}.\n")
        return True
    else:
        print(f"Checking: Error. Wrong argument name: {name}.\n")
        return False