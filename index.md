{% include cool_header.html %}
### AGH UST Kraków
### Wydział Fizyki i Informatyki Stosowanej
# Cząstki Elementarne i Oddziaływania - semestr letni 2024

## HOT NEWS! 
<!--
- Egzamin odbędzie się 20 czerwca o godzinie 11:15 w sali 108 D10.
- W dniach 6-10 czerwca 2022 r. w murach naszej Uczelni odbędzie się XIV Międzynarodowa Konferencja BEACH 2022, organizowanej przez zespół LHCb z Katedry Oddziaływań i Detekcji Cząstek WFiIS AGH. [Zapraszamy!](https://www.agh.edu.pl/konferencje/konferencja/article/beach-2022/)
- Magic beauty charmless decays: [przeczytaj ](https://lhcb-outreach.web.cern.ch/2022/03/17/magic-beauty-charmless-decays/)
[prezentacja Jakuba](Files/wykład-QCD-JWojnarowski.pdf)
 [Higgsy Filipa](Files/CEiO_Higgs_FBaran.pdf)
-->

## WYKŁADY
- Wprowadzenie [wykład](Files/wyklad_1_Introduction.pdf)
- Relatywistyka [wykład](Files/wyklad_2_relatywistyka.pdf)
- Wiązki, zderzenia, rozpady [wykład](Files/wyklad_3_zderzenia.pdf)
- Złota Reguła Fermiego [wykład](Files/wyklad_4_FGR.pdf)
- Oddziaływania elektromagnetycze [wykład](Files/wyklad_4_QED.pdf)
- Źródła cząstek o wysokich energiach  [wykład](Files/wyklad_4_zrodla.pdf)
- Rozpraszanie elektron-proton [wykład](Files/wyklad_5_ep.pdf)
- Model Kwarkowy [wykład](Files/wyklad_7_ModelKwarkowy.pdf) [problemy](Files/Zadania_2022_3.pdf)
- Charm & Beauty [wykład](Files/wyklad_8_CB.pdf)
- Oddziaływania silne [wykład](Files/wyklad_9_silne.pdf)   
- Oddziaływania słabe i elektrosłabe [wykład](Files/wyklad_10_EW.pdf)
  
<!--
- Fizyka na LHC [wykład](Files/LHC_Higgs.pdf),
- Oscylacje zapachu [wykład](Files/Flavour_oscillations.pdf)
-->
  
## ĆWICZENIA
- Relatywistyka  [Zadania](Files/Zadania_2022_1.pdf)
- Zderzenia [Zadania](Files/Zadania_2.pdf) 
- Ekperymentalne aspekty Modelu Standardowego [Zadania](Files/Zadania_2022_4.pdf)

### Zagadnienia do egzaminu 2024: [tutaj](Files/zagadnienia-2024.pdf)

- egzamin I termin: 10.06.2024, godz. 8:00.
- egzamin II termin: 3.07.2024 godz. 11, s 16/D10

## Literatura:
- Mark Thomson "Modern Particle Physics", University of Cambridge, 2013 [online resources](https://www.hep.phy.cam.ac.uk/~thomson/MPP/ModernParticlePhysics.html)
- Alessandro Bettini “Introduction to Elementary Particle Physics”  Cambridge University Press, 2014
- David Griffiths "Introduction to Elementary Particles", John Wiley & Sons 1987
- Donald H. Perkins "Introduction to High Energy Physics" (4th ed.) Cambridge University Press, 2000 [resources](doi:10.1017/CBO9780511809040)

<!--
- Oddziaływania słabe i elektrosłabe [wykład](Files/wyklad_10_EW.pdf)
- Fizyka na LHC [wykład](Files/wyklad_11_LHC_Higgs.pdf)
- Oscylacje zapachu [wykład](Files/Flavour_oscillations.pdf)
-->

## LABORATORIUM
- ROOT - różne techniki analizy na przykładzie rozpadu $J/\Psi$ na parę mionów (_taurus:/home/staff/mucha/Public/CEO_)
- Generacja przykładowego rozpadu: [zadanie](Files/Lab_CEO_TGenPS.pdf) - termin oddania: 28.05.2023

## PROJEKT
- Skąd się biorą cząstki w pliku z danymi? [Reconstruction](Files/LAB_reconstruction.pptx)
- Identyfikacja cząstek w eksperymencie LHCb [Identyfikacja](Files/Identyfikacja.pdf)
- Zadanie projektowe: Rekonstrukcja masy i wyznaczenie czasu życia mezonu $K^0_s$ i $\Lambda$ z danych zebranych przez eksperyment LHCb 
    1. Pliki z danymi umieszczone są w katalogu _taurus:/home/staff/mucha/Public/CEO/Projekt_
    2. Środowisko pracy: przeczytaj poniżej o dedykowanej instalacji VM i ROOTa
    3. Instrukcje, dane i przykłady rozwiązań zamieszczone są na współdzielonym dysku (AGH Google) CEO-2023
 - Termin oddania: 25.06.2023


### ROOT 
 You can find a plethora of ROOT tutorials:
 - Very recent [Manual](https://root.cern/manual/basics/)
 - Very clear and quite new tutorial with C++ and Pyhon [here](https://www.nevis.columbia.edu/~seligman/root-class/RootClass2021.pdf)
 - Examples with DataFrame [here](https://root.cern/doc/master/classROOT_1_1RDataFrame.html)
 - PyROOT Workshop z 2022, [zobacz](https://indico.cern.ch/event/882824/contributions/3929999/)
 
<!--
 - Some old pages:
   - [ROOT - basis](https://root.cern.ch/root/htmldoc/guides/primer/ROOTPrimer.html) or [primer](https://root.cern/primer/)
   - let's dive into ROOT from [here](https://root.cern.ch/root/htmldoc/guides/primer/ROOTPrimerLetter.pdf)
   - HASCO lectures and examples [2]:
       - [here](https://indico.cern.ch/event/704163/contributions/2936719/) (.cpp and .py examples)
       - [there](https://indico.cern.ch/event/788195/contributions/3364842/) (also .ipynb examples)
-->
 
### Working environment 
HEP analyses usually require [ROOT framework](https://root.cern/). 
> You can use ROOT on Windows but I strongly discourage you from doing this. 
> You can either:
- zainstalować VM z preinstalowanym ROOTem i condą (**podejście rekomendowane**), zobacz i pobierz [tutaj](https://figshare.com/s/2fd8f8072f9b7e50cf4d), kilka wskazówek praktycznych jest [tutaj](Files/notatki_VM_Root.pdf)
- use your personal computer with VM and install ROOT, see [here](https://root.cern/install/),
- używać ROOTa poprzez Google Collab: konfiguracja środowiska pracy podczas pracy w laboratorium WFiIS jest tutaj: [instrukcja](Files/WorkingEnv)
- używać ROOTAa na swoim lokalnym komputerze po zajęciach logując się na komputer w 204, instrukcja jest [tutaj](https://agile.fis.agh.edu.pl/confluence/pages/viewpage.action?pageId=28837229)



<!--
- upload our VM and become a happy user of well-configured VM, `ROOT` and `conda` application:<br>
   - [description](https://indico.fis.agh.edu.pl/event/1/contributions/88/attachments/62/102/Hands-on-WorkEnv.pdf),<br>
   - [Ubuntu VM from AGH Google Suite](https://drive.google.com/file/d/1fCczgh12l2z8Af-JJszyJlv-Tt14365z/view).
- "our" students can use our group server `lhcbd1` (access through `taurus.fis.agh.edu.pl`), you have both ROOT framowork, conda environment and data sets, see [here](lhcbd1.md),
-->

### How to start with Jupyter Notebook
- start with reading [this](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
- everything you need to know is [here](https://hsf-training.github.io/analysis-essentials/python/01basics.html#Jupyter)


### Python 
- practical course of Python, see [here](https://hsf-training.github.io/analysis-essentials/python/README.html)


### C++ or Py? This is the question...
> Well, why not trying both? Below you can find example of the same analysis in ROOT in C++ and Python scenario [3]:
   - [ROOT C++](Files/Tutorial-ROOT.pdf)
   - [PyROOT](Files/Tutorial-PyROOT_2018.pdf)
- Have a look at [PyROOT](https://root.cern/manual/python/) webpage.


<!--

## PROJEKT
- Skąd się biorą cząstki w pliku z danymi? [Reconstruction](Files/LAB_reconstruction.pptx)
- Identyfikacja cząstek w eksperymencie LHCb [Identyfikacja](Files/Identyfikacja.pdf)
- Materia-antymateria (łamanie CP) [OPIS](Files/projekt_2022.pdf)
- Zadanie projektowe [notatnik](https://github.com/lhcb/opendata-project/blob/master/LHCb_Open_Data_Project.ipynb)

- Kwarki [Zadania](Files/zadania_3.pdf)



## Particle Physics projects for AGH UST FPACS students
- Materia-antymateria (łamanie CP) [OPIS](Files/projekt_2021.pdf)

## HOT NEWS!
- Evidence of new physics (Measurement of the Positive Muon Anomalous Magnetic Moment) [web page](https://news.fnal.gov/2021/04/first-results-from-fermilabs-muon-g-2-experiment-strengthen-evidence-of-new-physics/) [article](Paper/muong2.pdf)
- Violation of lepton universality (Strengthened hints for a violation of lepton universality in B decays) [article](https://arxiv.org/abs/2103.11769)




<!--


## Goals of the course:
   I. Introduction to experimental particle physics. <br>
   II. Study of charm or beauty meson decays in the LHCb experiment with the use of real or simulated data. <br>
   III. Environment for daily work

### LHCb Experiment 
The LHCb (Large Hadron Collider beauty) experiment is one of the four main experiments that operate at the Large Hadron Collider (LHC) at CERN. The experiment is designed to study CP violation, observation of rare decays of beauty and charm particles, and search for New Physics (NP) evidences using indirect measurements. Whereas ATLAS and CMS are general-purpose detector with a broad physics programme spanning from the Standard Model (SM) though supersymmetry (SUSY) to extra dimensions, the LHCb detector is a single-arm forward spectrometer dedicated for studying flavour physics at the LHC. The LHCb programme is thus highly complementary to the direct searches performed at ATLAS and CMS. 

### D meson
D mesons contain charm quark. The lighter D<sup>+</sup> meson contains also one of the lightest quarks (up or down) whereas D<sub>s</sub><sup>+</sup> has a heavier strange quark. Decays of charm mesons involve the change of quark flavour through weak interaction. 

### Project 1: 3-body decay of D meson (real data)

### Project 2: D meson decays to three hadrons (simulated data)
1. Introduction:
   - study the channels of [D<sup>+</sup>](https://pdglive.lbl.gov/Particle.action?init=0&node=S031&home=MXXX035#decayclump_F) and [D<sub>s</sub><sup>+</sup>](https://pdglive.lbl.gov/Particle.action?init=0&node=S034&home=MXXX040#decayclump_A) decays and chose one that contains charge kaons or pions. 
   - draw Feynman diagram of your process and note whereas it is a common or rare decay (we call it favoured or suppressed decay). What type of interaction is responsible for this decay?
   - what information you need to obtain from experiment to observe your process?
2. Data anaysis:
   - study the data set (from AGH cloud, [check access to this site](https://dysk.agh.edu.pl/s/cQ6wLsdCxRjFpa4) ) <br> 
   It contains 160 000 simulated events of D<sup>+</sup> and D<sub>s</sub><sup>+</sup> decays to three hadrons (kaons and pions). 
   - Choose one mode of D meson decay, select candidates,
   - plot distribution of mass and life-time,
   - make fits and compare parameters with theory.
-->   



[1] LHCb Detector Performance, LHCb Collaboration, Roel Aaij et al. (Dec 19, 2014) [Int.J.Mod.Phys.A 30 (2015) 07, 1530022](https://arxiv.org/abs/1412.6352) <br>
[2] Hadron Collider Physics Summer School - [HASCO](http://hasco.uni-goettingen.de/)

