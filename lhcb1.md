{% include cool_header.html %}

## Serwer lhcb1

Instalacja FLUKI na swoim lokalmnym komputerze jest skomplikowana, w dodatku okazuje się, ze przewżnie działa ona tam wolno. <br>
Na potrzeby studentów FLUKA została zainstalowana na naszym grupowym serwerze, fizycznie znajdującym się w budynku D11. Można dostać się na niego np. z wydziałowego taurusa, używając darmowej aplikacji MobaXterm. Proszę zwrócić uwagę, czy w ustawieniach tej aplikacji aktywna jest opcja otwierania X terminala:

[!["moba"](Images/moba.png)](Images/moba.jpg)

Po uruchomieniu MobaXterm startujemy sesję ssh: `Sessions->SSH`. W oknie `Remote host` wpisujemy: `taurus.fis.agh.edu.pl`. W otwartym oknie można się zalogować na konto swojego zespołu:
```
ssh -XY hep-lab01@lhcb1
```
Nazwy kont to: 'hep-lab0X@lhcb1', gdzie X- oznacza numer zespołu. Hasła zostana podane na zajęciach. Prosze zauważyć, że przy wpisywaniu hasła kursor jest niewidoczny. 

## Repozytorium
Celem usprawnienia pracy i kontaktu pomiędzy zespołami i prowadzącym utorzone jest `Repozytorum`, czyli dostępne dla wszystkich miejsce, gdzie umieszczane są skrypty startowe, pliki z danymi, jak również można tam przesyłać swoje wyniki. Proszę sprawdzić dostęp:
```
ls -l /datab1/FLUKA/lab_repo
```
i z katalogu 'scripts' skopiować do swojego katalogu głównego '/home/hep-lab0X' skrypt 'setfluka':
```
cp /datab1/FLUKA/lab_repo/scripts/setfluka .
```

## Ustawienia środowiska 
Przed KAŻDYM rozpoczęciem pracy należy ustawić środowisko, czyli podać, skąd Fluka i Root mają pobierać bibliteki. Z repozytorum trzeba pobrać plik startowy `setfluka` i wykonać go:
```
source setfluka
```
## Zaczynamy!
Proszę najpierw założyć wygodną dla siebie strukturę katalogów. Uruchamiamy środowisko `Flair` komendą `Flair &` i przystępujemy do wykonania pierwszego zadania: [START](Start.md).
