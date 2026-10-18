import subprocess
from check_data import check_data_folder, check_data_file#, check_argument, check_receiptId
from flask import Flask, jsonify, request

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
    if len(request.args) == 1:
        # Tutaj muszę sprawdzić czy istnieje wywołany paraon
        print("Checking: Passed: Webservice called with 1 argument.")
        if 
        return jsonify({
            "status": "OK.",
            "kod błędu": "0",
            "opis": "Rozpoznano jeden parametr.",
        }), 200
    
    elif len(request.args) == 2:
        # Tutaj muszę sprawdzić czy odpytano o właściwy zakres danych
        print("Checking: Passed: Webservice called with 2 arguments.")
        return jsonify({
            "status": "OK.",
            "kod błędu": "0",
            "opis": "Rozpoznano dwa parametry.",
        }), 200        
    
    else:
        print("Checking: Error: Webservice called with bad number of arguments.")
        return jsonify({
            "status": "Błąd.",
            "kod błędu": "3",
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