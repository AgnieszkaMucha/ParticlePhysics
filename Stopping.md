{% include cool_header.html %}

### Projekt 1A
## Wyznaczenie zasięgu wysokoenergetycznych cząstek w różnych materiałach.
### Cel ćwiczenia:
Badanie oddziaływania promieniowania o wysokich energiach z materią, określenie różnicy w oddziaływaniu pomiędzy cząstkami lekkimi a ciężkimi, wyznaczenie zależności zasięgu promieniowania od energii, rodzaju promieniowania i materiału.

### Wykonanie ćwiczenia:
1. Napisz plik inputowy do FLUKI. Szybki starter do puszczenia symulacji jest [tutaj](https://agnieszkamucha.github.io/OPJzM/Start.html).
 Oddziaływanie będzie badane w cylindrze wypełnionym lekkimi i ciężkimi materiałami. Rozmiary należy tak dobrać, aby widoczny był zasięg promieniowania (można poszukać w tablicach). Źródłem będzie wiązka:
- Protonów i neutronów (cząstki ciężkie).
- Elektronów i fotonów (cząstki lekkie). <br>
Energię należy dobrać samodzielnie, z zakresu od 100 MeV do 100 GeV w kilku dowolnych, ale dających znaczące wyniki, krokach. 

2. Wykonaj symulację:
- dla wybranej wiązki cząstek: jednej ciężkiej (proton) i jednej lekkiej (elektron), 
- zbiornik wypełnij dwoma rodzajami materiałów: lekkim (np. powietrze, woda, krzem) i ciężkim (wolfram, ołów, żelazo, beton). 
- wybierz do scoringu estymatory: całkowitej zdeponowanej energii, energii promieniowania elektromagnetycznego, energii zdeponowanej przez promieniowanie pierwotne i dawki. O estymatorach we Fluce przeczytasz [tutaj](https://agnieszkamucha.github.io/OPJzM/Estymatory.html).
- liczba cząstek w wiązce nie powinna być mniejsza niż 10 tysięcy.

### Dyskusja wykonanej symulacji:
Dokonaj porównania wyników:
- jakie są różnice w oddziaływaniu poszczególnych cząstek? 
- jakie cząstki wtórne powstały?
- od czego zależą straty jonizacyjne?

### Opracowanie wyników (do 28 czerwca 2019):
- każda osoba powinna wykonać symulację oddziaływania wiązki protonów i elektronów w lekkich i ciężkich materiałach. Liczba padających cząstek to conajmniej 10 tysięcy, a cykli symulacji conajmniej 3. Energia wybrana z przedziału 0.1 - 1 GeV.
- proszę zrobić dwuwymiarowe rozkłady zdeponowanej energii (lub dawki) dla tego samego materiału i wskazać różnice pomiędzy elektronami i protonami, 
- w przypadku protonów: <br>
a) dla conajmniej trzech energii i dwóch materiałów zrobić rozkład zdeponowanej energii (lub dawki) w funkcji odległości i  wyznaczyć zasięg, <br>
b) zrobić rozkład (log-log) zasięgu w funkcji energii, porównać z wartościami tablicowymi. Uwaga: zasięg przedstawiamy w [cm], ale częściej jako iloczym zasięgu i gestości: [cm g/cm3 = g/cm²] (p. wykład). <br>
c) sprawdzić "skalowanie zasięgu", tzn, czy stosunek zasięgów (dla tych samych energii i tych samych cząstek) jest równy stosunkowi gęstości i pierwiastka z liczby atomowej (p. wykład), 
- dla elektronów: <br>
a) zrobić rozkład 2D i 1D energii zdeponowanej tylko przez wiązki pierwotne (BEAM_PART), <br>
b) zrobić rozkład 2D i 1D energii całkowitej zdeponowanej przy przejściu elektronów i skomentować różnicę z poprzednim rozkładem. <br>
c) wyznaczyć drogę radiacyjną lub zasięg i porównać z tablicami. Droga radiacyjna dla elektronów jest to odległość, po której energia elektronu, tracona w wyniku promieniowania hamowania, wynosi średnio 1/e (czyli około 36,8%) swej energii początkowej, wyrażana jest również jako wartość pomnożona przez gęstość materiału w [g/cm²]. 

### Ćwiczenia dodatkowe:
1. Beam dump dla LHC:
- proszę obliczyć, jaką energię (w [J]) niesie ze sobą wiązka 10e11 protonów o energii 7 TeV. Ile gramów miedzi mogłaby ta energia stopić? Wyznacz, korzystając z głównego ćwiczenia, grubość bloku z betonu, w którym można "zrzucić" taką wiązkę. 
2. Detektor śladowy:
- proszę dodać do zbiornika z wodą 3 cienkie (0.5cm) płaszczyzny z krzemu, ustawione prostopadle do osi, w równych odległościach. Wyznacz w nich depozyty energii (w płaczczyźnie _xy_) pochodzące od wiązki protonów o energii 10 GeV. Liczba protonów w wiązce powinna być mała, np 10.

### Ciekawe linki:
- [Symulacja śladu elektronów w materii](http://www.slac.stanford.edu/~rfc/egs/advtool.html)
- [Symulacje dla jonów](http://www.srim.org/#SRIM)
