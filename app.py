import subprocess
from check_data import check_data_folder, check_data_file, check_receiptId, check_arguments
from flask import Flask, jsonify, request
from receipts import get_receipt

subprocess.run("cls", shell=True, check=True)
print("Info: Program started.")

check_data_folder()
check_data_file()

# Tworzę obiekt app, który jest instancją klasy Flask.
webservice = Flask(__name__)
# ustawiam parametry wyświetlania wyników JSON
webservice.json.ensure_ascii = False
webservice.json.sort_keys = False
webservice.json.compact = False


@webservice.route("/receipts")
def receipts():
    if len(request.args) == 1 and check_arguments(request.args, 1): 
        # Tutaj muszę sprawdzić czy istnieje wywołany paraon
        subprocess.run("cls", shell=True, check=True)
        print("Checking: Passed: Webservice called with 1 argument.")
        print(check_arguments(request.args, 1))
        return jsonify({
            "status": "OK.",
            "kod błędu": "3",
            "opis": "Rozpoznano jeden parametr.",
        }), 200
    
    elif len(request.args) == 2 and check_arguments(request.args, 2):
        # Tutaj muszę sprawdzić czy odpytano o właściwy zakres danych
        subprocess.run("cls", shell=True, check=True)
        print("Checking: Passed: Webservice called with 2 arguments.")
        print(check_arguments(request.args, 1))
        return jsonify({
            "status": "OK.",
            "kod błędu": "4",
            "opis": "Rozpoznano dwa parametry.",
        }), 200        
    
    else:
        subprocess.run("cls", shell=True, check=True)
        print("Checking: Error: Webservice called with wrong number of arguments.")
        return jsonify({
            "status": "Błąd.",
            "kod błędu": "5",
            "opis": "Podany zły parametr wywołania."
        }), 200
         
     







# Obsłużę end point / i o nim zapomnę bo to jeszcze nic nie wnosi, takie "Hello Word!"
@webservice.route("/")
def root_page():
    if  len(request.args) == 0:
            return jsonify({
                "status": "Sukces.",
                "kod błędu": 0,
                "opis": "Witaj w serwisie pragonów fiskalnych."
            }), 200
    return jsonify({
        "status": "Błąd.",
        "kod błędu": "1",
        "opis": "Nie wywołano usługi."
    }), 200
if __name__ == "__main__":
    print("Info: Webservice is starting")
    webservice.run(debug=True)