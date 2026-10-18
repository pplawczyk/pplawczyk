# To jest moja biblioteka funkcji, które sobie napiszę na potrzeby webservice
# Wygodnym wydaje się utrzenie obiektu "paragon", który będzie reprezentował pojedyńczą instancję paragonu, którą odczytam z pliku.
# Następnie wczytując paragon po paragonie "przechodzić" między nimi tak by wygodnie na nich pracować.
# Chcę mieć funkcje:
# 1. sprawdź czy paragon o danym ID istnieje in:(id_paragonu), out:(boolean)
# 2. odpytaj o paragony z danego zakresu in:(datefrom, dateto), out:(list[id_paragonów...])
#
# Do obsługi plików JSON "element" po "elemencie" (item) potrzebuje biblioteki ijoin
import ijson
#
# Sprawdź czy istnieje paragon o podanym ID
def ask_if_receipt_exists(receipt_id):
    # najpierw otworzę sobie plik z danymi do odczytu jako plik binerny bo tego wymagan ijson
    # with zapewnia mi, że dopóki nie zamknę tego segmentu plik pozostnie otwarty, a po jego zamknięciu python samodzielnie ten plik zamknie
    with open("data/receipts.json", "rb") as file:

        for receipt in ijson.items(file, "receipts.item"):
            if receipt["document"]["receiptId"] == receipt_id:
                return True

    return False