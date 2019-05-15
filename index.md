
# Laboratorium Oddziaływania Promieniowania Jonizującego z Materią

## Cel laboratorium:
   I. Badania oddziaływania fotonów, ciężkich i lekkich cząstek naładowanych i neutralnych, o niskich i wysokich energiach, z różnymi rodzajami materiałów (symulacja programem FLUKA).

   II. Wyznaczenie depozytów energii i odpowiedzi mikropaskowego detektora VELO ze spektrometru LHCb (symulacja w architekturze GEANT i dane rzeczywiste - praca na ntuplu w architekturze ROOT).

## Wymagania dla studentów:
Laboratorium odbywać się będzie w godz. 8-10:30 w terminach: 8.05, 15.05, 22.05, 29.05 (sala 207/D10) .

Podczas zajęć w pracowni komputerowej, studenci zapoznają się z tematem ćwiczeń i pobiorą potrzebne pliki z danymi i przykładowe programy do analizy.
Podczas ćwiczeń studenci będą te programy modyfikować. Omówione zostaną szczegóły analizy.

Na podstawie przeprowadzonych analiz studenci wykonają samodzielnie dwa projekty (szczegóły projektu sa  [TUTAJ](Stopping.md):
1. Symulację oddziaływania promieniowania z materią programem FLUKA. Każda grupa wykonuje inny projekt z listy:
- oddziaływanie i wyznaczenie zasięgu cziąstek ciężkich (protonów, jonów) w różnych materiałach,
- oddziaływanie i wyznaczenie zasięgu elektronów i fotonów w różnych materiałach,
- oddziaływanie i wyznaczenie zasięgu neutronów w różnych materiałach,
2. Analizę depozytów energii w detektorze VELO.

## Warunki wstępne 
Upewnij się, że posiadasz konto na serwerze `lhcb1`, na którym zainstalowane są programy do przeprowadzenia symulacji (FLUKA) i  analizy danych (ROOT), tam umieszczone są zasoby do ćwiczeń. Sprawdź [konto na lhcb1](lhcb1.md) teraz!

## Ćwiczenia laboratoryjne I:
1. [Start-zaczynamy pracę z FLUKĄ](Start.md)
2. Szczególowy opis kategorii kart FLUKI: 
   - [`PRIMARY`](Primary.md)
   - [`GEOMETRY`](Geometry.md) [Hands-on](https://agnieszkamucha.github.io/OPJzM/Files/Geometry.pdf)
   - [`MEDIA`](Media.md)
3. Podstawowe estymatory:
   - [`USRBIN`](Estymatory.md) [Hands-on](https://agnieszkamucha.github.io/OPJzM/Files/Scoring.pdf)
4. [Ratunku! Nic nie działa!](Ratunek.md)

## Ćwiczenia laboratoryjne II:
1. [ROOT - praktyczne wprowadzenie](Root.md)
2. [VELO](Velo.md) 

## Projekty
1. Zasięg wysokoenergetycznych cząstek naładowanych w różnych materiałach (Fluka), [opis](Stopping.md). <br>
2. Zależnośc strat joinizacyjnych dE/dx od masy czątek i rodzaju materiału.
3. VELO, [opis](VELO.md).

## Dodatki
1. [Fluka 2 ROOT](Floot.md)
