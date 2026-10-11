# Zbiór 1000 paragonów fiskalnych

## Zawartość

Zestaw składa się z trzech powiązanych plików:

- `fiscal_receips.json` – dane 1000 paragonów,
- `fiscal_receipsschema.json` – JSON Schema Draft 2020-12 dla całego zbioru i pojedynczego paragonu,
- `README.md` – opis struktury, założeń i reguł kontroli.

## Charakter danych

Plik zawiera syntetyczne dane przeznaczone do testowania integracji, importu, eksportu, walidacji i obliczeń. Struktura przypomina dane biznesowe paragonów, ale nie jest oficjalnym formatem urządzenia fiskalnego ani protokołem wymiany z CRK.

## Parametry zbioru

- liczba paragonów: 1000,
- okres sprzedaży: od 1 sierpnia 2026 do 10 października 2026 włącznie,
- data sprzedaży: rzeczywista data kalendarzowa,
- godziny sprzedaży: 06:00–23:59 oraz 00:00–00:59,
- waluta: PLN,
- tryb obsługi: DINE_IN,
- kanał: IN_STORE,
- metoda płatności: CARD,
- NIP nabywcy na każdym paragonie: 5210088110,
- liczba pozycji na paragonie: od 1 do 12,
- rabaty i kupony: brak,
- stawki VAT występujące w katalogu: 5%, 8% i 23%.

## Rozkład restauracji i kas

- REST-001: 130 paragonów, KASA-01,
- REST-002: 510 paragonów, po 255 dla KASA-02 i KASA-03,
- REST-003: 360 paragonów, po 180 dla KASA-04 i KASA-05.

Każda kasa ma własną sekwencję pola `receiptNumber`.

## Struktura główna

Plik danych jest pojedynczym obiektem JSON:

```json
{
  "datasetVersion": "1.0.0",
  "generatedForSchemaVersion": "1.0.0",
  "receiptCount": 1000,
  "generationParameters": {},
  "receipts": []
}
```

Każdy element tablicy `receipts` jest kompletnym paragonem.

## Reprezentacja kwot i ilości

Kwoty są tekstami dziesiętnymi z dwoma miejscami po przecinku:

```json
"grossAmount": "47.98"
```

Ilości są tekstami z trzema miejscami po przecinku:

```json
"quantity": "2.000"
```

W kodzie należy używać typu dziesiętnego, np. `Decimal`, a nie `float`.

## Reguły biznesowe do dodatkowej walidacji

JSON Schema weryfikuje strukturę i formaty. Poniższe zależności trzeba sprawdzać w logice aplikacji:

```text
grossAmountBeforeDiscount = quantity × unitGrossPrice
grossAmount = grossAmountBeforeDiscount − totalDiscountAmount
item.vat.netAmount + item.vat.vatAmount = item.grossAmount
totals.netAmount = suma vatSummary[].netAmount
totals.vatAmount = suma vatSummary[].vatAmount
totals.grossAmount = suma vatSummary[].grossAmount
totals.netAmount + totals.vatAmount = totals.grossAmount
totals.amountDue = totals.grossAmount
paymentSummary.amountApplied = totals.amountDue
paymentSummary.changeAmount = 0.00
paymentSummary.remainingAmount = 0.00
fiscalDevice.uniqueNumber = fiscalInformation.fiscalUniqueNumber
```

Ponadto:

- `lineNumber` powinien być unikalny w obrębie paragonu,
- `receiptId`, `transactionId`, `sourceDocumentId` i `paymentId` powinny być unikalne,
- data `saleDateTime` powinna mieścić się w zadanym okresie,
- `issuedDateTime` nie powinno być wcześniejsze niż `saleDateTime`,
- NIP powinien przejść kontrolę sumy kontrolnej,
- liczba elementów tablicy `receipts` powinna odpowiadać `receiptCount`.

## VAT

Pole `ratePercent` przyjmuje w tym zbiorze wartości:

- `5.00`,
- `8.00`,
- `23.00`.

Odpowiadają im modelowe kody fiskalne `C`, `B` i `A`. Mapowanie ma charakter testowy i nie powinno być automatycznie przenoszone do systemu produkcyjnego bez uzgodnienia z konfiguracją urządzeń oraz zespołem podatkowym.

## Walidacja w Pythonie

```python
import json
from jsonschema import Draft202012Validator, FormatChecker

with open("schema.json", encoding="utf-8") as file:
    schema = json.load(file)

with open("fiscal-receipts-1000-realistic.json", encoding="utf-8") as file:
    dataset = json.load(file)

validator = Draft202012Validator(
    schema,
    format_checker=FormatChecker()
)

errors = sorted(
    validator.iter_errors(dataset),
    key=lambda error: list(error.path)
)

if errors:
    for error in errors:
        print(list(error.path), error.message)
else:
    print("Plik jest zgodny ze schematem.")
```

## Kodowanie

Pliki są zapisane w UTF-8. Nazwy produktów nie zawierają symboli znaków towarowych takich jak `®`, `©`, `™` i `℠`.
