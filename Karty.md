#### [HOME OPJzM](https://agnieszkamucha.github.io/OPJzM/)
## Kategoria `PRIMARY'
W niej definiowane są parametry żródła promienowania - rodzaj, pęd lub energię, kształt. Określamy również liczbę wychodzących czątek i _seed_ symulacji:

[!["Primary"](Images/primary.jpg)](Images/primary.jpg)
```
BEAM 
```
definiuje wielkości charakteryzujące wiązkę: typ cząstek, energię lub pęd, rozbieżność i profil wiązki.<BR>
Poszczególne pola, w których definiuje się parametry źródła nazywane są we Fluce `What[N]`, _N_ jest to numer parametru, w oryginalnym inpucie Fluki (bez Flaira) był to numer zarezerwowanego 8-znakowego pola, w którym umieszczało się liczbową lub znakową wartość parametru do symulacji. Obecnie Flair podpowiada w rozwijanej liście możliwe paramery i  możemy dokonać następujących ustaleń:
[!["Beam"](Images/beam.jpg)](Images/beam.jpg)

`WHAT(1)` wybrać typ wiązki. Możliwość wyboru: Momentum (pęd) lub Energy (energia), (Function – nieaktywne) <br> 
- p: podać średni pęd cząstek wiązki (w GeV/c) <br>
- E: podać średnią energię cząstek wiązki (w GeV) <br>
Wartość domyślna dla pędu to 200.0 GeV/c  

`WHAT(2)`	
- Δp: wybrać rozkład dla pędu. Możliwość wyboru: Flat (płaski) lub Gauss. Dla pędu zaleca się wybór rozkładu płaskiego (jednorodnego). <br>
- ΔE: wybrać rozkład dla energii Flat (płaski) lub Gauss.<br>
	- Flat Δp: podać niepewność pędu (w GeV/c).
	- Gauss Δp(FWHM): podać szerokość połówkową (FWHM = 2,355σ) rozkładu Gaussa. 
	
`What(3)` określa rozbieżność wiązki w mrad. 	
- Δφ: wybrać rozkład kątowy rozbieżności wiązki. Możliwość wyboru: Flat (płaski), Gauss lub Isotropic (izotropowy). 
	- Flat, Gauss- Δφ: podać wartość rozbieżności kątowej (od 0 do 1999).
	- Isotropic- oznacza rozbieżność wiązki >2π rad 

`WHAT(4)` określa szerokość wiązki w cm.	
- Shape(X): wybrać kształt wiązki w kierunku X. Możliwość wyboru: Rectangular (prostokątny), Annular (kątowy) lub Gauss. (Function – nieaktywne). 
	- Rectangular	Δx: podać szerokość wiązki w kierunku osi X.
	- Annular	Rmin: podać minimalny promień wiązki o kształcie kątowym
	- Gauss		x(FWHM): podać szerokość połówkową wiązki o kształcie gaussowskim w kierunku osi X

`WHAT(5)` określa szerokość wiązki w cm	
- Shape(Y):	wybrać kształt wiązki w kierunku Y. Możliwość wyboru: Rectangular (prostokątny), Annular (kątowy) lub Gauss. (Function – nieaktywne). 
	- Rectangular	Δy: podać szerokość wiązki w kierunku osi Y.
	- Annular	Rmax: podać maksymalny promień wiązki o kształcie kątowym
	- Gauss		y(FWHM): podać szerokość połówkową wiązki o kształcie gaussowskim  w kierunku osi Y
	
`WHAT(6)`
Wartość ignorowana

`SDUM'  
Part:	wybrać nazwę cząstek żródła lub wiązki:
`4-HELIUM`:	cząstka alfa
`RAY`	cząstka nierzeczywista, oznaczająca prostoliniową trajektorię, wykorzystywaną do skanowania geometrii
`PROTON	proton
`ELECTRON`	elektron
`PHOTON`	foton
`NEUTRON`	neutron
`BEAMPART`	cząstki bezpośrednie/wiązka padająca

