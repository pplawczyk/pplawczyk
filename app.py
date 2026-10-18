import subprocess
from check_data import check_data_folder, check_data_file
from webservice import webservice_start
from flask import Flask, jsonify, request
from werkzeug.serving import make_server

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
    if len(request.args) == 0:
        return jsonify({
        "status": "Błąd.",
        "kod błędu": "2",
        "opis": "Nie podano parametrów."
    })
    else:
             
        return jsonify({
            "status": "OK",
            "parametry": request.args.to_dict()
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