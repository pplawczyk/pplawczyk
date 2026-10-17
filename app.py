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
# ensure_ascii to paremetr podklasy json, który zmienia sposób obłsugi znaków narodowych
webservice.json.ensure_ascii = False
# sort_keys to parametr podklasy json, który wymusza sortowanie parametrów podawanych prze JSON w odpowiedzi, daje to większą czytelność chociaż teoretycznie nie jest to do końca poprawne bo API odwołuje się po kluczach, a nie indeksach
webservice.json.sort_keys = False



# Obsłużę end point / i o nim zapomnę bo to jeszcze nic nie wnosi
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
        "kod błędu": "2",
        "opis": "Nie wywołano usługi."
    })

if __name__ == "__main__":
    print("Info: Webservice is starting")
    webserver = make_server("127.0.0.1", 5000, webservice)
