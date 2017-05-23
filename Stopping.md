{% include cool_header.html %}

### Projekt 1A
## Wyznaczenie zasięgu wysokoenergetycznych cząstek w różnych materiałach.
### Cel ćwiczenia:
Badanie oddziaływania promieniowania o wysokich energiach z materią, określenie różnicy w oddziaływaniu pomiędzy cząstkami lekkimi a ciężkimi, wyznaczenie zależności zasięgu promieniowania od energii, rodzaju promieniowania i materiału.

### Wykonanie ćwiczenia:
1. Napisz plik inputowy do FLUKI. Szybki starter do puszczenia symulacji jest [tutaj](https://agnieszkamucha.github.io/OPJzM/Start.html).
 Oddziaływanie będzie badane w prostopadłościanie wypełnionym lekkimi i ciężkimi materiałami. Rozmiary należy tak dobrać, aby widoczny był zasięg promieniowania (można poszukać w tablicach). Źródłem będzie wiązka:
- Protonów, jonów (złota, olowiu, węgla) lub neutronów (cząstki ciężkie).
- Elektronów lub fotonów (cząstki lekkie).

Energię należy dobrać samodzielnie, z zakresu od 100 MeV do 100 GeV w sześciu dowolnych, ale dających znaczące wyniki, krokach. 
2. Wykonaj symulację:
- dla wybranej wiązki cząstek: jednej ciężkiej i jednej lekkiej. 
- Zbiornik wypełnij dwoma rodzajami materiałów: lekkim (np. powietrze, woda, krzem) i ciężkim (ołów, żelazo, beton). 
- Wybierz do scoringu estymatory: całkowitej zdeponowanej energii, energii promieniowania elektromagnetycznego, energii zdeponowanej przez promieniowanie pierwotne i dawki. O estymatorach we Fluce przeczytasz [tutaj](https://agnieszkamucha.github.io/OPJzM/Estymatory.html).
- Liczba cząstek w wiązce nie powinna być mniejsza niż 10 tysięcy.

### Opracowanie ćwiczenia:
Dokonaj porównania wyników:
- jakie są różnice w oddziaływaniu poszczególnych cząstek? 
- jakie cząstki wtórne powstały?
- od czego zależą straty jonizacyjne?
- Przedstaw sprawozdanie z najbardziej znaczącymi wynikami.

Wyznacz zasięg promieniowania:
- zrzutuj rozkłady 2D na 1D, skomentuj wynik.
- jeśli to możliwe wyznacz: zasięg, drogę radiacyjną, 
- gdyby wiązka uderzała przez godzinę, jaka dawka zdeponuje się w materiale?

### Ćwiczenia dodatkowe:
1. Beam dump dla LHC:
- proszę obliczyć, jaką energię (w [J]) niesie ze sobą wiązka 10e11 protonów o energii 7 TeV. Ile gramów miedzi mogłaby ta energia stopić? Wyznacz, korzystając z głównego ćwiczenia, grubość bloku z betonu, w którym można "zrzucić" taką wiązkę. 
2. Detektor śladowy:
- proszę dodać do zbiornika z wodą 3 cienkie (0.5cm) płaszczyzny z krzemu, ustawione prostopadle do osi, w równych odległościach. Wyznacz w nich depozyty energii (w płaczczyźnie _xy_) pochodzące od wiązki protonów o energii 10 GeV. Liczba protonów w wiązce powinna być mała, np 10.

### Ciekawe linki:
- [Symulacja śladu elektronów w materii](http://www.slac.stanford.edu/~rfc/egs/advtool.html)
- [Symulacje dla jonów](http://www.srim.org/#SRIM)
