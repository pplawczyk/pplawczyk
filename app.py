import subprocess
from check_data import check_data_folder, check_data_file, check_arguments_no
from flask import Flask, jsonify, request
from receipts import get_receipt, get_receipts_list

subprocess.run("cls", shell=True, check=True)
print("Info: Program started.\n")

check_data_folder()
check_data_file()

# Tworzę obiekt app, który jest instancją klasy Flask.
webservice = Flask(__name__)
# ustawiam parametry wyświetlania wyników JSON
webservice.json.ensure_ascii = False
webservice.json.sort_keys = False
webservice.json.compact = False

# Tutaj obsługuje endpoint /receipts
@webservice.route("/receipts")
def receipts():
    
    # Zaczynam od sprawdzenia czy podano właściwą liczbę argumentów
    if check_arguments_no(request.args):
        
        # dla uproszczenia w tej zmiennej trzymam sobie listę wywołanych argumentów 
        arguments = list(request.args)    
        
        # Skoro liczba argumentów się zgadza to robię sprwadzenia czy jest 1 i obsługuję ten przypadek
        if len(request.args) == 1:
            print(f"Info: Number of arguments is: {len(request.args)}.\n")
            
            # Sprawdź czy wywołany argument to receiptId.
            if next(iter(request.args)) == "receiptId":
                arguments = list(request.args)
                print(f"Checking: Passed: Called argument is: {arguments[0]}\n")

                # Skoro wywołany argument jest poprawny to przejdź do szukania paragnu o zadanym Id
                receipt = get_receipt(request.args.get("receiptId"))
                if receipt == False:
                    return jsonify({
                        "status": "OK.",
                        "kod": "5",
                        "opis": "Nie znaleziono paragonu o zadanym UUID."
                    }), 200
                else:
                    return jsonify(receipt)

            else:
                # Argumentem nie jest receiptId więc kończę błędem
                print("Checking: Error. Called argument not recognized.\n")
                return jsonify({
                        "status": "OK.",
                        "kod": "4",
                        "opis": "Podano argument o niewłaściwej nazwie."
                    }), 200
        
        elif len(request.args) == 2:
            # dla wygody tworzę sobie zmienne, które przechowują wartości wywołania endpoint
            date_from = request.args[arguments[0]]
            date_to = request.args[arguments[1]]
            print(f"Info: Two called arguments are: {arguments[0]} = {date_from}, {arguments[1]} = {date_to}\n")
            get_receipts_list(date_from , date_to)
        return jsonify({
        "status": "OK.",
        "kod": "2",
        "opis": "Podano właściwą liczbę argumentów."
    }), 200

    else:
        print("Kończę pracę bo wywołano niewłaściwe argumenty.")
        return jsonify({
        "status": "Błąd.",
        "kod": "3",
        "opis": "Podano niewłaściwą liczbę argumentów."
        }), 200



     
     







# Obsłużę end point / i o nim zapomnę bo to jeszcze nic nie wnosi, takie "Hello Word!"
@webservice.route("/")
def root_page():
    if  len(request.args) == 0:
            return jsonify({
                "status": "Sukces.",
                "kod": 0,
                "opis": "Witaj w serwisie pragonów fiskalnych."
            }), 200
    return jsonify({
        "status": "Błąd.",
        "kod": "1",
        "opis": "Nie wywołano usługi."
    }), 200


# Tutaj uruchamiam webserwice
if __name__ == "__main__":
    print("Info: Webservice is starting.\n")
    webservice.run(debug=True)