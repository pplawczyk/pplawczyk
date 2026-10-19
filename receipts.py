# To jest moja biblioteka funkcji, które sobie napiszę na potrzeby webservice
# Wygodnym wydaje się utrzenie obiektu "paragon", który będzie reprezentował pojedyńczą instancję paragonu, którą odczytam z pliku.
# Następnie wczytując paragon po paragonie "przechodzić" między nimi tak by wygodnie na nich pracować.
# Chcę mieć funkcje:
# 1. sprawdź czy paragon o danym ID istnieje in:(id_paragonu), out:(boolean)
# 2. odpytaj o paragony z danego zakresu in:(datefrom, dateto), out:(list[id_paragonów...])
#
# Do obsługi plików JSON "element" po "elemencie" (item) potrzebuje biblioteki ijoin
import ijson
from pathlib import Path
import uuid


#
# Sprawdź czy istnieje paragon o podanym UUID

def get_receipt(receipt_id: str) -> bool:
    file_path = Path(__file__).resolve().parent / "data" / "receipts.json"
    searched_receipt_id = str(receipt_id).strip().lower()

    with file_path.open("rb") as file:
        for receipt in ijson.items(file, "receipts.item"):
            current_receipt_id = (
                str(receipt.get("document", {}).get("receiptId", ""))
                .strip()
                .lower()
            )

            if current_receipt_id == searched_receipt_id:
                return True

    return False