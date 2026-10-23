# To jest moja biblioteka funkcji, które sobie napiszę na potrzeby webservice
# Wygodnym wydaje się utrzenie obiektu "paragon", który będzie reprezentował pojedyńczą instancję paragonu, którą odczytam z pliku.
# Następnie wczytując paragon po paragonie "przechodzić" między nimi tak by wygodnie na nich pracować.
# Chcę mieć funkcje:
# 1. sprawdź czy paragon o danym ID istnieje in:(id_paragonu), out:(boolean)
# 2. odpytaj o paragony z danego zakresu in:(datefrom, dateto), out:(list[id_paragonów...])
#

import ijson                                    # do obsługi plików JSON "element" po "elemencie" (item)
from pathlib import Path                        # do obsługi ścieżek w katalogach
import uuid                                     # do obsługi formatu UUID
from flask import Flask, jsonify                # do obsługi webservice
from datetime import datetime                   # do obsługi formatów dat ISO 8601
from check_data import check_uuid, check_date   # moje funkcje do sprawdzania różnych danych
#
# Sprawdź czy istnieje paragon o podanym UUID

# w tej funkcji sprawdzam czy w pliku z pragaonami znajduje się paragon o podanym UUID i jeśli go znajdę to zwrócę jego zawartość
def get_receipt(receipt_id):
        # Sprawdzam czy w wyołaniu funkcji id paragonu jest w formacie UUID 
        if not check_uuid(receipt_id):
            print(f"Checking: Error: Value: \"{receipt_id}\" is not in UUID format.\n")
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
                print(f"Current UUID: {saved_receipt_id}")
                if saved_receipt_id == receipt_id:
                    print(f"UUID found!: {saved_receipt_id}\n")
                    return receipt

        return False


def get_receipts_list(date_from: str, date_to: str) -> list:
    print(f"Czy pierwszy argument to data?: {check_date(date_from)}")
    return True