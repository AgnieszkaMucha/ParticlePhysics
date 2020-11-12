{% include cool_header.html %}
## Particle Physics project for AGH UST FPACS students
# D meson decays to three hadrons
## Goals of the course:
   I. Introduction to experimental particle physics. <br>
   II. Search for D meson decay in data simulated in the LHCb experiment. <br>
   III. Environment for daily work

### LHCb Experiment 
The LHCb (Large Hadron Collider beauty) experiment is one of the four main experiments that operate at the Large Hadron Collider (LHC) at CERN. The experiment is designed to study CP violation, observation of rare decays of beauty and charm particles, and search for New Physics (NP) evidences using indirect measurements. Whereas ATLAS and CMS are general-purpose detector with a broad physics programme spanning from the Standard Model (SM) though supersymmetry (SUSY) to extra dimensions, the LHCb detector is a single-arm forward spectrometer dedicated for studying flavour physics at the LHC. The LHCb programme is thus highly complementary to the direct searches performed at ATLAS and CMS. 

### D meson
D mesons contain charm quark. The lighter D meson contains also one of the lightest quarks (up or down) whereas Ds has a heavier strange quark. Decays of charm mesons involve the change of quark flavour through weak interaction. 

### Project
1. Introduction:
   - study the channels of [D](https://pdglive.lbl.gov/Particle.action?init=0&node=S031&home=MXXX035#decayclump_F) and [Ds](https://pdglive.lbl.gov/Particle.action?init=0&node=S034&home=MXXX040#decayclump_A) decays and chose one that contains charge kaons or pions. 
   - draw Feynman diagram of your process and note whereas it is a common or rare decay (we call it favoured or suppressed decay).
   - what information you need to obtain from experiment to observe your process.
2. Data anaysis:
   - study the data set: 
   It contains 160 000 simulated events of D and Ds decays to three hadrons (kaons or pions). 
   
### Working environment 
HEP analysis usually require [ROOT framework](https://root.cern/). <br>
You can use ROOT on Windows but I strongly discourage you from doing this. <br>
Instead you can either:
- use our group server `lhcbd1` (access through taurus), see [here](lhcbd1.md),
- use your personal computer with VM and install ROOT, see [here](https://root.cern/install/),
- upload our VM and become a happy user of well-configured VM, ROOT and conda application:<br>
   - [description](https://indico.fis.agh.edu.pl/event/1/contributions/88/attachments/62/102/Hands-on-WorkEnv.pdf),<br>
   - [Ubuntu VM from AGH Google Suite](https://drive.google.com/file/d/1fCczgh12l2z8Af-JJszyJlv-Tt14365z/view).

### ROOT 
 You can find a plethora of ROOT tutorials. 
 - Let's start with some basis:[ROOT - basis]() 
 - All you need to do in ROOT is described in HASCO lectures and examples [2]:
   - (here)[https://indico.cern.ch/event/704163/contributions/2936719/] and 
   - (there)[https://indico.cern.ch/event/788195/contributions/3364842/] 
 
### C++ or Py? This is the question...
Well, why not trying both? Below you can find example of the same analysis in ROOT in C++ and Python scenario [3]. 
 




[1] LHCb Detector Performance, LHCb Collaboration, Roel Aaij et al. (Dec 19, 2014) [Int.J.Mod.Phys.A 30 (2015) 07, 1530022](https://arxiv.org/abs/1412.6352) <br>
[2] Hadron Collider Physics Summer School - [HASCO](http://hasco.uni-goettingen.de/)

