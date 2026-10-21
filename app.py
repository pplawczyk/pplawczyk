import subprocess
from check_data import check_data_folder, check_data_file, check_arguments_no, check_arguments_name
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
    if check_arguments_no(request.args):
        
        if len(request.args) == 1:
             #sprawdź czy wywołany argument to ten właściwy. Oczekuje receiptId skoro jest 1.
             print("Czy właściwy argument?: ", check_arguments_name(request.args, "receiptId"))
             if check_arguments_name(request.args, "receiptId"):
                print("Obsłuż zapytanie o 1 paragon.")

             else:
                print("Jeden argument ale o złej nazwie. Kończe to.")
                return jsonify({
                        "status": "OK.",
                        "kod": "4",
                        "opis": "Podano argument o niewłaściwej nazwie."
                    }), 200
        
        elif len(request.args) == 2:
            print("Wywołano 2 argument. Obsłuż to.")

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
if __name__ == "__main__":
    print("Info: Webservice is starting")
    webservice.run(debug=True)