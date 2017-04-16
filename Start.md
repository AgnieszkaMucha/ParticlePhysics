#### [HOME](https://agnieszkamucha.github.io/OPJzM/)
## Co to jest FLUKA?
FLUKA jest narzędziem ogólnego zastosowania, służącym do obliczeń transportu promieniowania i symulacji oddziaływania promieniowania z materią.
FLUKA jest historycznym programem do projektowania osłon w reaktorach jądrowych, ale obecnie symulacje promieniowania we FLUCE przeprowadzane są wszędzie, gdzie mamy doczynienia z dużymimi strumieniami, począwszy od przestrzeni kosmicznej, a skończywszy na Eksperymentach Fizyki Wysokich Energii, w szczególności  w przygotowywanym na 2023 roku programie High Lumininosity Large Hadron Collider. <br>
Przykad możliwości Fluki można zobaczyć poniżej. Na rysunkach przedstawiono oddziaływanie wiązki protonów o energii 10 GeV z wodą  i krzemowym sensorem (rozkład przedstawia energię zdeponowaną przez hadrony)  oraz dawkę promieniowania zdeponowaną w materiale spektrometru LHCb.

[!["Dawka"](Images/PR.png)](Images/PR.png)
Może dziwić fakt, ale FLUKA napisana jest w języku Fortran, a użytkownik przeprowadza symulację wykorzystując przygotowane narzędzia, bez ingerencji w kod programu. Praca we Fluce odbywa się poprzez interfejs  FLAIR. Interfejs FLAIR ułatwia edycję plików wsadowych, uruchomienie kodu i wizualizację plików wynikowych. Napisany został w oparciu o standard Tkinter Pythona.

Zakres możliwości aplikacyjnych programu FLUKA obejmuje m. in. przyspieszanie wiązki protonów lub elektronów, projektowanie geometrii tarczy i zastosowanych osłon, obliczenia kalorymetryczne, dozymetryczne, projektowanie detektorów, planowanie radioterapii, itd.
FLUKA pomaga symulować z wysoką dokładnością oddziaływania i propagację promieniowania w materii, z wykorzystaniem 60 różnych cząstek oraz odpowiadających im antycząstek, a także neutronów o energiach od energii termicznych. Program może również symulować transport fotonów spolaryzowanych (np. promieniowanie synchrotronowe) oraz fotonów optycznych. FLUKA ma możliwość śledzenia cząstek naładowanych (także w obecności pól elektrycznych i magnetycznych). <br>
Szczegółowe informacje dotyczące programu FLUKA i FLAIR można znaleźć [tutaj](http://www.fluka.org/fluka.php). <br>


## Jak rozpocząć pracę z programem FLUKA na WFiIS AGH? 
- Ze swojego konta na `taurusie` należy zalogować się na konto zespołu na serwerze `lhcb1`. Problem z kontem? Sprawdź [lhcb1](lhcb1.md).
- Na `lhcb` wykonać skrypt startowy:
```bash
$ source setlhcb
```
- Stworzyć i przejść do swojego katalogu roboczego:
- Uruchomić program FLAIR komendą:
```bash
$ flair &
```
Popatrzymy najpierw na niezbędne elementy pliku do wykonania symulacji:

## Moja pierwsza symulacja
Praca w programie FLUKA polega na tworzeniu plików wsadowych (INPUT). Można go edytować w dowolnym edytorze, ale znacznie wygodniej używać do tego Flaira. Flair umożliwia stworzenie nowego pliku na podstawie wbudowanych szablonów symulacji: `basic, decay, no geometry, itp` porzez:
```
Input->New->basic
```
W ten sposób dostajemy podpowiedź, z czego powinien się składać plik inputowy i możemy go dostosować do własnego problemu.

Plik wsadowy INPUT jest tworzony w standardzie ASCII z rozszerzeniem `.inp` .
Plik INPUT składa się z komend (opcji), każda z nich zawiera jedną lub więcej linii (z przyczyn historycznych nazywanych „kartami”). Poza komendami FLUKI plik wsadowy powinien także zawierać opis geometrii projektowanej symulacji.
Typowa struktura pliku INPUT:
- tytuły i komentarze,
- opis geometrii (bryły przestrzenne i powierzchnie, w połączeniu z przestrzenią podzieloną na regiony (obowiązkowe),
-	definicje materiałów (obowiązkowe, za wyjątkiem materiałów wstępnie zdefiniowanych w programie),
-	przypisanie materiałów do danych regionów (obowiązkowe),
-	definicje potrzebnych detektorów, 
Detektor jest to region, w którym użytkownik chce obliczać wartości oczekiwane wielkości fizycznych, takich jak energia zdeponowana, dawka, fluencja, itp. Dostępne są różne typy detektorów odpowiadające różnym wielkościom i różnym algorytmom zastosowanym do oszacowania tych wartości (estymatory). Wybór detektorów jest opcjonalny, jednak należy wybrać przynajmniej jeden.
-	definicje źródeł cząstek (obowiązkowe),
-	zdefiniowane ustawienia charakteryzujące problem, czyli np. wartości graniczne energii, efekty fizyczne nie symulowane domyślnie, cząstki wyłączone z transportu, itp.  (opcjonalne),
-	inicjalizacja losowej sekwencji liczbowej (obowiązkowe, jeśli wymagane jest oszacowanie błędu statystycznego),
-	sygnał startowy i liczba żądanych zdarzeń (obowiązkowe).
 
## Tworzenie pliku inputowego
Po lewej stronie okna Flaira znajduje się drzewo projektu. Widoczne są w nim następujące kategorie kart:
- `General`:	karty ogólne (TITTLE, DEFAULTS, GLOBAL, …). Mają wprowadzone wartości domyślne. Jeśli nie – można wpisać tytuł.
- `Primary`:	karty z opisem wiązki i cząstek pierwotnych (tzw. _primaries_). Tutaj zdefiniujemy parametry źródła promieniowania - typ, kształt, pęd, energię, rozmycie. Określimy rodzaj - fotony, protony, itd. Określamy też liczbę cząstek pierwotnych, liczba ta ma ogromny wpływ na czas wykonania zadania.
- `Geometry`:	karty z opisem geometrii, regionów, w któych badamy promieniowanie. To jedna z najważniejszych kategorii - z dostępnych figur geometrycznych (kula, sfera, prostopadłościan, walec, płaszczyzny, i.in.), wykorzystując logiczne operatory sumowania, odejmowania, budujemy `Regiony`, czyli naszą rzeczywistość - detektor, osłony, człowieka, itp.
- `Media`:	karty definiujące zastosowane materiały. Tutaj określamy, z czego składają się zbudowane powyżej `Regiony` - można wykorzystać bazę ze zdefinowanymi we Fluce materiałami (woda, miedź, powietrze, itp), można stworzyć swój składnik podając skład chemiczny (np. papier).
- `Physics`:	karty definiujące właściwości fizyczne dotyczące danej symulacji.
- `Transport`:	karty, które zmieniają sposób transportu cząstek w programie FLUKA.
- `Biasing:`	karty definiujące obciążenie estymatorów. <br>
W tych trzech ostatnich kartach można podać modele fizyczne oddziaływań, które chcemy, aby znalazły się w transporcie cząstek. Domyślnie Fluka używa aktualnych modeli i teorii, można to zmienić w wyjątkowych zastosowaniach, ale na początku lepiej tu nic nie zmieniać, o fizykę we Fluce dbają znakomici eksperci z różnych dziedzin, zajmujący się fizyką w BAAARDZO szerokim zakresie energetycznym.
- `Scoring`:	karty definiujące zakres i rodzaj estymatorów. Jest to druga najważniejsza kategoria - definiujemy, jakich wyników (estymatorów parametrów fizycznych) oczekujemy od Fluki. Bardzo dużo możliwości - od depozytów energii do strumieni i fluencji cząstek. W osobnym rozdziale opisane zostaną  najbardziej dla nas użyteczne [estymatory](Estymatory.md). 

Poszczególne karty można traktować jak pojedyncze obiekty. Można je kasować, wstawiać, kopiować, wklejać, klonować, … Pozycja karty nie ma większego znaczenia. FLAIR stara się reorganizować plik Input podczas zapisywania i przesuwa karty na odpowiednie pozycje. Karty z kategorii Geometry, powinny się znaleźć w bloku GEOBEGIN .. GEOEND.
Aby rozpocząć edycję karty, należy wybrać kartę za pomocą strzałek góra/dół lub za pomocą myszy. Karta aktywna ma podświetlone tło w jasnożółtym kolorze i czarną obramówkę. Można "podświetlić" kilka (takich samych) kart i wtedy zmienimy wszystkie karty (uwaga, żeby nie zmienić nazw estymatorów). <br>
Uwaga! We Flairze ZAWSZE trzeba wpisywać liczby z kropką dziesiętną na końcu, np. `100.`, nawet liczby całkowite! To pozostałość po fortranie... <br>

Nasze pierwsze kroki postawimy robiąc symulację przejścia wiązki protonów przez beczkę z wodą. Najlepiej tej plik skonstruować samemu, ale na pierwszy raz możemy posłużyć się gotowym przykładem. W tym celu  we Flairze wczytujemy przygotowany input `beczka.inp` klikając w przyciski: `Input->Load`. 
Widok na konsoli powinien wyglądąć tak:

[!["FLAIR"](Images/Flair.png)](Images/Flair.png)

### STOP
Tutaj proponujemy się zatrzymać i poeksperymentować. Zadanie na pierwsze ćwiczenia laboratoryjne polega na stworzeniu pliku inputowego, otrzymaniu kilku (pięciu?) rozkładów i dyskusji wyników. 

### Błędy w pliku inputowym
Podczas tworzenia inputu, popełnimy na pewno szereg błędów. Najpierw trzeba sprawdzić, czy Flair sam ich nie znalazł - zmieni kolor czcionki na czerwono, trzeba poprawić! Czasem w trakcie pisania pojawi się czerwonawe okienko sygnalizujące `Error`, patrzymy dlaczego i poprawiamy. Ale przeważnie błąd zauważymy w momencie wykonania symulacji, albo dopiero po - gdy oglądniemy wyniki. Jest to bardzo irytujące - w sytuacjach kryzysowych, zanim rzucisz klawiaturą, spojrzyj na: [Pomocy!](Ratunek.md) Fluka ma swoje ograniczenia, czasem wynikające z jej fortranowskiego pochodzenia, ale czasem również z Gnuplota, którego Flair używa do tworzenia wykresów.

## Wykonanie symulacji
Po stworzeniu pliku inputowego puszczany symulację klikając:
```
Run->Runs->Start
```
Można zuważyć, że zadanie wykonuje się w tzw. cyklach - im większa liczba cykli, tym mniejsze niepewności statystyczne. Podczas wykonania możemy śledzić status zadania:
[!["STATUS"](Images/Flair_run.jpg)](Images/Flair_run.jpg)

Po uzyskaniu wiadomości `Finished OK` możemy oglądnąć wyniki. Jeśli dostaniemy cokolwiek innego, np: `TIMEOUT` - mamy błąd w pliku inputowym (najczęściej: za dużo przedziałów w rozkładach 3D, brak kropki po liczbie całkowitej, niezdefiniowany materiał, region, itp). Wracamy do `Input` i zaczynamy analizę i poprawę  pliku. Może się tu zdarzyć, że `TIMEOUT` ma przyczynę systemową - brak biblioteki. Staramy się to sprawdzać, ale historia nas nauczyła, że takie zdarzenia pojawiają się nieoczekiwanie. 

Gdy jest `Finished OK`, kliknijmy na: `Run->Files` i `Run->Data`- zobaczymy pliki outputowe. Widać w nazwach numery _jednostek logicznych_, które zdefiniowaliśmy w pliku inputowym, zauważymy również, że Fluka zapisała wyniki OSOBNO dla każdego cyklu. Jest to pozostałość po zamierzchłych czasach, kiedy komputery liczyły wolno i często się zawieszały - w takiej sytuacji można było wykorzystać fragment skończonej symulacji. Po zastanowieniu wydaje się to logiczne. 

Musimy teraz połączyć wyniki. W tym celu klikamy `Run->Data->Process` i czekamy na zielone okienko informujące, ile i jakie pliki outputowe są łączone. Widok powinien być taki:

[!["PROCESS"](Images/Flair_megre.png)](Images/Flair_megre.png)

### Błędy po wykonaniu symulacji
Chociaż symulacja skończyła się prawidłowo, możemy przy procesowaniu wyników dostać znowu  czerwonawe okienko z `Errors` zamiast zielonego z sukcesem `Data Merging`. Błędy na tym etapie spowodowane są błędami w geometrii - np. obszar do `Scoringu` wykracza poza region w `Geometry`, albo regiony są źle nazwane lub zdefinowane, albo coś jest źle z zakresami rozkładów. Musimy to znaleźć sami i puścić symulację od nowa. 

Może tutaj pojawić się błąd z `Gnuplota` - np, że ma za małą paletę barw. Wtedy administrator powinien zainstalować jego inną wersję. Może się również zdarzyć, że brakuje danych na rozkładzie - wtedy Gnuplot nie ma co wyświetlić. W tej sytuacji po prostu zwiększamy liczbę `Primaries`. 

Gdy symulacja skończy się szybko i dostaniemy na końcu uspokajające potwierdzenie `Finisked OK`, możemy nie zauważyć, że w rzeczywistości nic się nie wykonało. Na skutek niezauważonych błędów w `Inpucie`, symulacja się zakończyła bez wyników, ale zauważyć to można dopiero patrząc na `Run->Files` - w oknie będzie tylko numer jednego cyklu zamiast np. pięciu. Znowu wracamy do inputu i szukamy blędu... 

## Wykonanie rozkładów
Uff, już niedługo... <br> Klikamy `Plot->Oz` i widzimy listę stworzonych przez nas rozkładów. Feel free to click! <br>
Proszę teraz przyjrzeć się informacjom wypisanym w oknie Flaira i przetestować wszystkie możliwe przyciski! Fluka ma naprawdę ogromne możliwości...

[!["PLOT"](Images/Flair_plot.png)](Images/Flair_plot.png)


### Wskazówki praktyczne
- Kilka rysunków na jednej konsoli można zrobić zwiększająć licznik w przycisku `Display`.
- Jeśli chcemy zrobić rozkłady w NOWEJ sesji Flaira, wczytujemy plik inputowy: `Input->Load`, a potem musimy połaczyć dane `Run->Data->Process` i zrobić rysunki: `Plot->Oz`.
- Jeśli dokonaliśmy zmian w inpucie (np. energii), a po wykonaniu symulacji dostaliśmy dokładnie takie same rozkłądy, jak w poprzednim zadaniu, nie zawsze oznacza to, że oddziaływnie jest dokładnie takie samo. Raczej Flair wziął do procesowania wyników poprzednie pliki... Najlepiej po dokonaniu zmian w inpucie otworzyć nową sesję Flaira. Jeszcze lepiej - przed wykonaniem nowej symulacji usunąć wszystkie stare pliki.

## Dyskusja wyników
Dzisiejsze laboratorium skończymy, gdy KAŻDY uczestnik dostanie rozkłady i omówi je z prowadzącym. 

# Dla dociekliwych
1. Symulację można wykonć z konsoli, bez Flaira, komendą:
```
rfluka -M 5 beczka
```
2. Proszę oglądnąć (w edytorze lub Flairze: `Run->Data->Files->Cycles->data->Viewer`) pliki z wynikami. Co w nich jest? Jakie informacje? Jak zapisane? Czy po "wyklikaniu" rysunków nie mamy ochoty zrobić ich w innym programie? <br>
Zapraszamy zatem do konwersji wyników Fluki do ROOTa [FLOOT](Floot.md)... 
3. Użytkownik Fluki nie może zmieniać źródeł (nawet ich oglądnąć), ale ma dostęp do wszystkich generowanych zmiennych, nawet tych, które nie są widoczne w standardowym procesingu. Do takich należą np. parametry wygenerownych cząstek wtórnych czy parametry śladów. Informacje o nich znajdują się w fortranowskich tablicach, zwanych COOMMONami i zdolny użytkownik może z nich zrobić rozkłady, patrz [tutaj](https://indico.cern.ch/event/489973/contributions/2000440/attachments/1272042/1972478/09_AdvancedUserRoutines2016.pdf). Jest jakiś chętny/chętna do spróbowania?









