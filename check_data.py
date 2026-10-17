# Tutaj utworzę sobie fukcje, którymi będę sprawdzał różne rzeczy przed uruchomieniem całego rozwiązania.
# Na początek sprawdzę czy mam dostęp do pliku JSON z paragonami

# pathlib to standartowa bibliotego pythona używana do pracy ze ścieżkami,
from pathlib import Path

# Zmienna, w której będę przechowywał folder w którym uruchamiam program
my_folder = ""
my_folder = Path(__file__).resolve().parent
print(my_folder)
