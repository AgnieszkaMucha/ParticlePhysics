## Ratunku! Nie działa!
Fluka i Flair mają swoje ograniczenia. Trudno ich uniknąć, kiedy z leciwego, fortranowskiego programu robimy podstawowe narzędzie do symulacji ogromnych, skomplikowanych systemów detekcyjnych. Jeśli, pomimo uważnej edycji, wyszukania błędów opisanych w Opisie [START](Start.md), nie możesz uzyskać wyników symulacji, albo nie działa Flair, spróbuj następujących działań:
1. Flair nie działa! 
-- Wykonaj skrypt startowy `$ source ~/setfluka`
2. Nie ma mojego inputu! Wczoraj tu był! 
- Poszukaj w innym katalogu, może w tzw. katalogu roboczym?
3. Symulacja nie chce odpalić! Przed chwilą działała! 
- Zacznij od nowego katalogu. Przekopiuj swój input do nowego, pustego katalogu i rozpocznij symulację. Flair tworzy pewną liczbę plików tymczasowych, czasem błędnie wykonana symulacja zostawia ślad i podczas procesowania danych ten błąd się wczytuje. Dotyczy to najczęściej błędów w binowaniu rozkładów.
4. Dodaję karty do `Scoringu`, a nie ma ich po symulacji!
- Zacznij od nowego, pustego katalogu lub usuń wszystkie utworzone pliki (oprócz `.inp` oczywiście)
