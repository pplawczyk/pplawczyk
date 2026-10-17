from flask import Flask, jsonify, request

# Tworzę obiekt app, który jest instancją klasy Flask.
webservice = Flask(__name__)

# ensure_ascii to paremetr podklasy json, który zmienia sposób obłsugi znaków narodowych
webservice.json.ensure_ascii = False
# sort_keys to parametr podklasy json, który wymusza sortowanie parametrów podawanych prze JSON w odpowiedzi, daje to większą czytelność chociaż teoretycznie nie jest to do końca poprawne bo API odwołuje się po kluczach, a nie indeksach
webservice.json.sort_keys = False


# Obsługa end point /recepipt
@webservice.route("/receipt")
def receipt():
    # na początek sprawdzę czy podano jakiekowliek parametry w zapytaniu HTTP GET
    if  len(request.args) == 0:
        return jsonify({
            "status": "Błąd.",
            "kod błędu": 1,
            "opis": "Nie podano parametrów."
        }), 400
    return jsonify({
        "status": "Sukces.",
        "parametry": dict(request.args)
    })


# Obsłużę end point /
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

# Obsługa end point /receipts
@webservice.route("/receipts")
def receipts():
    # na początek sprawdzę czy podano jakiekowliek parametry w zapytaniu HTTP GET
    if  len(request.args) == 0:
        return jsonify({
            "status": "Błąd.",
            "kod błędu": 1,
            "opis": "Nie podano parametrów."
        }), 400
    return jsonify({
        "status": "Sukces.",
        "parametry": dict(request.args)
    })

if __name__ == "__main__":
     webservice.run(debug=True)