# Importuje bibliotekę Flask, która dostarczy mi serwer webowy, który zasymuluje mi działanie API
from flask import Flask
# Importuje też funkcję jsonify, która obsługuje formaty JSON
from flask import jsonify
# Importuje też funkcję request, która pozwala mi pobierać dane z zapytań HTTP
from flask import request

# Tworzę obiekt app, który jest instancją klasy Flask. A że Flask jest serwerem webowym to mam teraz swój.
app = Flask(__name__)

# ensure_ascii to paremetr podklasy json, który zmienia sposób obłsugi znaków narodowych
app.json.ensure_ascii = False
# sort_keys to parametr podklasy json, który wymusza sortowanie parametrów podawanych prze JSON w odpowiedzi, daje to większą czytelność chociaż teoretycznie nie jest to do końca poprawne bo API odwołuje się po kluczach, a nie indeksach
app.json.sort_keys = False


@app.route("/receipts")
def receipts():
    # na początek sprawdzę czy podano jakiekowliek parametry w zapytaniu HTTP GET
    if  len(request.args) == 0:
        return jsonify({
            "status": "Błąd",
            "kod błędu": 1,
            "opis": "Nie podano parametrów"
        }), 400
    return jsonify({
        "status": "Sukces",
        "parametry": dict(request.args)
    })

if __name__ == "__main__":
    app.run(debug=True)