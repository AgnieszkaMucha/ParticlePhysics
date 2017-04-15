#### [HOME](https://agnieszkamucha.github.io/OPJzM/)
## Estymatory we Fluce
Rzeczywisty eksperyment przeprowadzamy w celu uzyskania konkretnych parametrów - energii zdeponowanej w pewnej objetości, policzenia produktów w zderzeniu, często w funkcji energii padającego promieniowania. Jak mamy czas i fundusze - eksperyment przeprowadzamy kilkakrotnia, a wyniki uśredniamy według zasad statystyki. 

Zamast przeprowadzenia rzeczywistego doświadczenia możemy zrobić jego symulację. O ile doświadczenie polegające na rzucie monetą jest dość łatwe do przewidzenia, to symulacje oddziaływania promieniwania z materią oparte są o metody Monte Carlo. Można bardzo ogólnie powiedzieć, że różnica jest w liczbie i stopniu pochodnych w równaniach... Ale ciągle dążymy do tego samego - na podstawie wielu eksperymentów (w MC opisanych równaniami) liczymy takie same parametry, jak w rzeczywistym ekspermencie. Jeżeli w danych rzeczywistych mówimy o wynikach - to w symulacji - o zmiennej losowej. A estymatory są to FUNKCJE zmiennych losowych. Najprostszym z nich jest średnia. Robiąc pomiar mówimy, że np. neutron stracił (2.0+-0.1) MeV/mm, a robiąc symulację powiemy raczej: estymator strat energii dla mionu wynosi (2.0+-0.1) MeV/mm. 

Obliczenia trasportu cząstek we Fluce umożliwiają wyznaczenie estymatorów szeregu parametrów, np. zdeponowanej energii, dawki, strumienia czy fluencji. Estymatory te so wbudowane i obliczane  na kilka sposobów, szczegóły można znaleźć na stronie [FLUKI](http://www.fluka.org/fluka.php?id=man_onl).

### Metoda estymacji we FLUCE
to do later!

## `USRBIN`
W naszych ćwiczeniach posłużymy się jednym z estymatorów: `USRBIN`. Pokazuje on np. depozyty energii w trójwymiarowej siatce, niezależnie od geometrii regionów. Fluka używa jednostek: cm, GeV. <br>
Użycie karty estymatora `USRBIN` wymaga:
- Wyboru współrzędnych - kartezjańskich, cylndrycznych, sferycznych.
- W zależności od rodzaju współrzędnych - podania ich zakresu (tu uwaga - zakres nie może być szerszy niż wymiary geometryczne całego obiektu).
- Wybrania parametru do estymacji. Jest tu cała lista, zachęcamy do testów. Najlepiej wpisać sobie kilka kart ze `USRBIN` z estymatorami różnych parametrów.
- Określenia numeru logicznego, najlepiej z rozwijanej listy, bo niektóre numery są zarezerwowane dla fortrana.
- Zdefiniowanie nazwy "detektora" - tak we Fluce nazywamy nasz estymator. Ta nazwa powinna być znacząca i może mieć do 8 znaków.
- Określenia liczby przedziałów (binów) każdej współrzędnej. Tutaj jest ograniczenie (na razie nie poznane dokładnie), ale jeśli problem jest symetryczny w płaszczyźnie _xy_, to nie ma potrzeby dzielić np. osi _x_ (damy tam jeden przedział). <br>
Gestość podziału wybierzemy doświadczalnie, od tego zależy rozdzielczość naszej symulacji. Jeżeli będziemy badać zasięg promieniowania na odległości np. 1m, to rozsądnie jest podzielić ją na 500 binów.  Pamiętajmy o kropce dziesiętnej po każdej liczbie całkowitej!

Przykład definiowania `USRBIN`:

[!["USRBIN"](Images/USRBIN.png)](Images/USRBIN.png)

Rozkłady uzyskane po symulacji to kolorowe wykresy 3D, o różnej zawartości. W naszych zastosowaniach wykorzystamy estymatory następujących zmiennych: _(dopisać opis)_
- `DOSE`
- `HAD_CHAR`
- `EM-ENERGY`
- `PROTON`, `NEUTRON`, `PHOTON`,  `ELECTRON`, `PIONS+-`, `MUONS`
- `SiMEVNE`

Paleta barw jest proporcjonalna do wartości estymowanej, a osie na wykresach pokazują geometryczne zakresy binowania. <br>
WAŻNE! We Fluce WSZYSTKIE wyniki liczbowe podawane są w odniesieniu do JEDNEJ cząstki padającego promieniowania (zwanego tu `Primaries`). <br>
Przyjrzyjmy się (dłużej) i omówmy, co znajduje się na poniższych wykresach:

