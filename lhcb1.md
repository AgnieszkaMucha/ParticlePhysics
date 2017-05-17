{% include cool_header.html %}

## Serwer lhcb1

Instalacja FLUKI na swoim lokalnym komputerze jest skomplikowana, a w dodatku okazuje się, że przewżnie działa ona tam wolno. <br>
Na potrzeby studentów FLUKA została zainstalowana na naszym grupowym serwerze, fizycznie znajdującym się w budynku D11. Można dostać się na niego np. z wydziałowego `taurusa`, używając darmowej aplikacji `MobaXterm`lub z dowolnego terminala w sysemie linux. 
Używając MobaXterm, proszę zwrócić uwagę, czy w ustawieniach tej aplikacji aktywna jest opcja otwierania X terminala:

[!["moba"](Images/moba.jpg)](Images/moba.jpg)

Po uruchomieniu `MobaXterm` startujemy sesję ssh: `Sessions->SSH`. W oknie `Remote host` wpisujemy: `taurus.fis.agh.edu.pl`.
Dalej już postępuje się tak samo niezależnie, czy mamy okno z linuxa, czy z Moby:  logujemy na konto swojego zespołu:
```
ssh -XY hep-lab0X@lhcb1
```
Nazwy kont to: `hep-lab0X@lhcb1`, gdzie X- oznacza numer zespołu. Hasła zostaną podane na zajęciach. Prosze zauważyć, że przy wpisywaniu hasła kursor jest niewidoczny. 

## Repozytorium
Celem usprawnienia pracy i kontaktu pomiędzy zespołami i prowadzącym utworzone jest `Repozytorum`, czyli dostępne dla wszystkich miejsce, gdzie umieszczane są skrypty startowe, przykłady, pliki z danymi, jak również można tam przesyłać swoje wyniki. Proszę sprawdzić dostęp:
```
ls -l /datab1/FLUKA/lab_repo
```
i z katalogu `scripts` skopiować do swojego katalogu głównego `/home/hep-lab0X` skrypt `setfluka`:
```
cp /datab1/FLUKA/lab_repo/scripts/setfluka .
```

## Ustawienia środowiska 
Przed KAŻDYM rozpoczęciem pracy należy ustawić środowisko, czyli podać, skąd Fluka i Root mają pobierać biblioteki. Z repozytorum trzeba pobrać plik startowy `setfluka` i wykonać go:
```
source setfluka
```
## Zaczynamy!
Proszę najpierw założyć wygodną dla siebie strukturę katalogów. Uruchamiamy środowisko `Flair` komendą:
```
Flair &
```
i przystępujemy do wykonania pierwszego zadania: [START](Start.md).

## Uwaga!
Konto na serwerze `lhcb1` jest przeznaczone tylko na cele dydaktyczne dla analiz dotyczących oddziaływania promieniowania z materią i fizyki cząstek elementarnych. Inne użycie jest niedozwolone!
