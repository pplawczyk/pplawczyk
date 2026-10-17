## Projekt na zaliczenie 1 semestru wykładów z programowania w pythonie

<!--
**pplawczyk/pplawczyk** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Opis problemu.

Od 1 stycznia 2027 roku wchodzi nowa regulacja Ministerstwa Finansów dotycząca obsługi paragonów z NIP.
Paragony z NIP do wartości 450 zł (100 EUR) przestają być traktowane jak faktura uproszczona.
Oznacza to, że za każdym razem jak konsument poda numer NIP można założyć, że transakcja ma formułę B2B i należy wystawić fakturę VAT.
Faktury powinny być rejestrowane w KSeF. 
Rejestracja faktury w KSeF odbywa się poprzez przygotowanie pliku xml spełniającego wymagania tzw. faktury ustrukturyzowanej oraz przesłanie go do systemu KSeF.

Chce się nauczyć:
1. Jak sięgać po dane wejściowe (paragony) zgromadzone w jakimś źródle, może to być:
- baza danych, bo znam podstawy baz danych takich jak MySQL i języka zapytań SQL
- jakiś web service, nie znam ale chętnie się nauczę jak tego używać i wydaje mi się to bardziej atrakcyjne 
2. Jak przetwarzać dane:
- weryfikować ich poprawność np. czy NIP jest poprawny
- wyliczać stawki odpowiednie stawki VAT dla różnych typów produktów
3. Jak przygotować poprawne dane wyjściowe:
- tworzenie plików XML
- obsługa formatowanie charakterystyczne dla XML
4. Jak wysłać taki plik gdzieś do systemu docelowego. Nie mam pojęcia jeszcze co i jak w tym obszarze. 

Co robię w tej chwili:
Z1 - Wygenerowałem sample data w postacji JSON z 1000 paragonami
Z2 - Uruchomie web service, który sprawdza czy wywołano jakieś parametry na / oraz /receipts
Open: nie wiem czy potrzebne jest obsłużenie wszystkich możliwych wywołań strony tak by nie zwracała 404 Not Found. Na potrzeby nauki raczej nic więcej mi to nie wnosi.
Z3 - Dodam obsługę plików. Tak by móc czytac plik z paragonami.
Open: jaką metodę wybrać? Przeglądanie całego pliku przy każdym zapytaniu do webservice wydaje się być mało eleganckim rozwiązaniem. Najlepiej wydaje się wczytywać jakoś paragon po paragonie, sprawdzać paragaon różnymi warunkami i przygotować wynik w postaci listy z ID. Nie wiem jak wygodnie zwrócić taki wynik.
-->
