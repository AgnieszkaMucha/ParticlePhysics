#### [HOME](https://agnieszkamucha.github.io/OPJzM/)

### Projekt 1A
## Wyznaczenie zasięgu wysokoenergetycznych cząstek w różnych materiałach.
### Cel ćwiczenia:
Badanie oddziaływania promieniowania o wysokich energiach z materią, określenie różnic pomiędzy cząstkami lekkimi a ciężkimi, wyznaczenie zależności zasięgu promieniowania od energii, rodzaju promieniowania i materiału.

### Wykonanie ćwiczenia:
1. Napisz plik inputowy do FLUKI. Oddziaływanie będzie badane w prostopadłościanie wypełnionym lekkimi i ciężkimi materiałami. Rozmiary należy tak dobrać, aby widoczny był zasięg promieniowania (można poszukać w tablicach). Żródłem będzie wiązka:
- Protonów lub neutronów (cząstki ciężkie).
- Elektronów lub fotonów (cząstki lekkie).
Energię należy dobrać samemu, z zakresu od 100 MeV do 100 GeV w sześciu dowolnych, ale dających znaczące wyniki krokach. 
2. Wykonaj symulację:
- dla wybranej wiązki cząstek: jednej ciężkiej i jednej lekkiej. 
- Zbiornik wypełnij dwoma rodzajami materiałów: lekkim (np. powietrze, woda) i ciężkim (ołów, żelazo, beton). 
- Wybierz do scoringu estymatory: całkowitej zdeponowanej energii, energii promieniowania elektromagnetycznego, dawki i  fluencji hadronów. 
- Liczba cząstek w wiązce nie powinna być mniejsza niż 10 tysięcy.

### Opracowanie ćwiczenia:
Dokonaj porównania wyników:
- jakie są różnice w oddziaływaniu poszczególnych cząstek? 
- jakie cząstki wtórne powstały?
- od czego zależą straty jonizacyjne?
Wyznacz zasięg promieniowania:
- zrzutuj rozkłady 2D na 1D, skomentuj wynik.

### Ćwiczenia dodatkowe:
1. Beam dump dla LHC:
- proszę obliczyć, jaką energię (w [J]) niesie ze sobą wiązka 10e11 protonów o energii 7 TeV. Ile gramów miedzi mogłaby ta energia stopić? Wyznacz, korzystając z głównego ćwiczenia, grubość bloku z betonu, w którym można "zrzucić" taką wiązkę. 
2. Detektor śladowy:
- proszę dodać do zbiornika z wodą 3 cienkie (0.5cm) płaszczyzny z krzemu, ustawione prostopadle do osi. Wyznacz w nich depozyty energii (w płaczczyźnie _xy_). 
