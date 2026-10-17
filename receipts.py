# To jest moja biblioteka funkcji, które sobie napiszę na potrzeby webservice
# Wygodnym wydaje się utrzenie obiektu "paragon", który będzie reprezentował pojedyńczą instancję paragonu, którą odczytam z pliku.
# Następnie wczytując paragon po paragonie "przechodzić" między nimi tak by wygodnie na nich pracować.
# Chcę mieć funkcje:
# 1. sprawdź czy paragon o danym ID istnieje in:(id_paragonu), out:(boolean)
# 2. odpytaj o paragony z danego zakresu in:(datefrom, dateto), out:(list[id_paragonów...])
#
#
#
#

def check_receipe(id_receipe):
    """Zwraca True, jeśli identyfikator istnieje paragon o danym ID."""
    if id_receipe is None:
        return False
    return bool(str(id_receipe).strip())