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
Z1 - Generuje sample data, które będą reprezentować paragony:
     - używam formuł Excela
     - dane wyexportuje do plików CSV - jeszcze nie wiem czy to docelowa forma ale póki co to dla mnie wygodny format
     - 1000 sameple records, z okresu: <01.08.2026 , 10.10.2026>
     - dane z 3 lokali: lokal A: 1 kasa, lokal B: 2 kasy, lokal C: 2 kasy 

-->
