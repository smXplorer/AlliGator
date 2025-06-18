.. _alligator-bibliography:

Bibliography
============

The following publications have used AlliGator or discuss topics of relevance 
(see article summary to see which category they belong to).
Please consider citing [XM25]_ if you are using AlliGator in your work.

Most of them are available for 
free on `PubMed <https://pubmed.ncbi.nlm.nih.gov/?term=xavier+michalet>`_ or 
`eScholarship <https://escholarship.org/search?q=xavier%20michalet&searchType=
eScholarship&searchUnitType=series>`_

Ref. [RC12]_ discusses the phasor ratio concept (borrowed from the Gratton lab, where Ryan 
Colyer came from) in the context of a custom-build time-resolved photon-counting 
camera.

Ref. [KC18]_ is the first peer-reviewed publication introducing AlliGator 
(developed for that work) and demonstrates its use for the analysis of time-gated 
data of in vivo FRET acquired with an ICCD camera. The 
supporting information of this article contains an extensive tutorial on phasor 
analysis, as well as details on data analysis with AlliGator, which can be 
found `here <https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.
1002%2Fjbio.201800185&file=jbio201800185-sup-0002-SupInfo.pdf>`_.

Data used in this work can be found `here 
<https://doi.org/10.6084/m9.figshare.5561872.v1>`_, `here 
<https://doi.org/10.6084/m9.figshare.5776890.v2>`_, `here 
<https://doi.org/10.6084/m9.figshare.5786694.v2>`_, `here 
<https://doi.org/10.6084/m9.figshare.5788128.v2>`_, and `here 
<https://doi.org/10.6084/m9.figshare.5791476.v4>`_.

Ref. [AU19]_ describes the use of AlliGator for time-gated decay fitting of data 
acquired with SwissSPAD2, a custom time-gated CMOS SPAD array (with large gates). 
The limited phasor analysis presented in this article was done with a MATLAB code 
developed by Arin Ulku.

Ref. [RA20]_ discussed in vitro analysis of visible range fluorescence data 
acquired with SwissSPAD2, the time-gated CMOS SPAD array introduced in [AU19]_. 
This article is associated with data than can be used to test a number of features 
of AlliGator.

Ref. [AU20]_ presents more characterization of SS2 using AlliGator, as well as 
custom MATLAB code, with associated data.

Ref. [XM21]_ used AlliGator for some data illustrating this manuscript (but not 
central to the paper, which is concerned with theoretical considerations on 
phasor analysis).

Ref. [JS22]_ uses AlliGator for both phasor and NLSF (1-exponential and 
2-exponential fits) analysis. A number of features were introduced to simplify 
the analysis, specifically multi-RO and single-pixel analysis and the Fit 
Parameter Map, the single-exponential phasor loci (SEPL) representation, as well as 
significant performance improvements.

Ref. [XM22]_ is a proceedings paper using AlliGator to analyze data where the 
gate width is larger than the laser period and demonstrates that phasor analysis 
works just as well in those cases.

Ref. [XM23]_ is another proceedings paper using AlliGator to analyze data acquired 
with SwissSPAD3, which has shorter gates than the laser period and shows that 
phasor analysis works equally well for most cases, although the photon budget 
decreases for short gates.

Ref. [DR24]_ uses AlliGator for FLIM data analysis, focusing on amplitude-averaged 
lifetime computed from phasor analysis.

Ref. [XM25]_ describes AlliGator's features, architecture and open source release.

.. rubric:: References

.. [RC12] Ryan A. Colyer, Oswald H.W. Siegmund, Anton S. Tremsin, John V. Vallerga, Shimon Weiss, Xavier Michalet, "Phasor imaging with a widefield photon-counting detector, Journal of Biomedical Optics 17 (2012) 016008. `doi:10.1117/1.JBO.17.1.016008 <https://doi.org/doi:10.1117/1.JBO.17.1.016008>`_

.. [KC18] Sez‐Jade Chen, Nattawut Sinsuebphon, Alena Rudkouskaya, Margarida Barroso, Xavier Intes, Xavier Michalet, "In vitro and in vivo phasor analysis of stoichiometry and pharmacokinetics using short‐lifetime near‐infrared dyes and time‐gated imaging", Journal of Biophotonics 12  (2019) e201800185, `doi:10.1002/jbio.201800185 <https://doi.org/10.1002/jbio.201800185>`_

.. [AU19] Arin Can Ulku, Claudio Bruschini, Ivan Michel Antolovic, Yung Kuo, Rinat Ankri, Shimon Weiss, Xavier Michalet, Edoardo Charbon, "A 512 × 512 SPAD Image Sensor With Integrated Gating for Widefield FLIM", IEEE Journal of Selected Topics in Quantum Electronics 25 (2019) 6801212, `doi: 10.1109/JSTQE.2018.2867439 <https://doi.org/10.1109/JSTQE.2018.2867439>`_

.. [RA20] Rinat Ankri, Arkaprabha Basu, Arin Can Ulku, Claudio Bruschini, Edoardo Charbon, Shimon Weiss, Xavier Michalet, "Single-Photon, Time-Gated, Phasor-based Fluorescence Lifetime Imaging Through Highly Scattering Medium", ACS Photonics 7 (2020) 68-79, `doi: 10.1021/acsphotonics.9b00874 <https://doi.org/10.1021/acsphotonics.9b00874>`_

.. [AU20] Arin Ulku, Andrei Ardelean, Michel Antolovic, Shimon Weiss, Edoardo Charbon, Claudio Bruschini, Xavier Michalet, "Wide-field time-gated SPAD imager for phasor-based FLIM applications", Methods and Applications in Fluorescence 8 (2020) 024002, `doi: 10.1088/2050-6120/ab6ed7 <https://doi.org/10.1088/2050-6120/ab6ed7>`_

.. [XM21] Xavier Michalet, "Continuous and discrete phasor analysis of binned or time-gated periodic decays", AIP Advances 11 (2021) 035331, `doi: 10.1063/5.0027834 <https://doi.org/10.1063/5.0027834>`_

.. [JS22] Jason T. Smith, Alena Rudkouskaya, Shan Gao, Juhi M. Gupta, Arin Ulku, Claudio Bruschini, Edoardo Charbon, Shimon Weiss, Margarida Barroso, Xavier Intes, Xavier Michalet, "In vitro and in vivo NIR Fluorescence Lifetime Imaging with a time-gated SPAD camera", Optica 9 (2022) 532, `doi: 10.1364/OPTICA.454790 <http://dx.doi.org/10.1364/OPTICA.454790>`_

.. [XM22] X. Michalet, A. Ulku, J. Smith, C. Bruschini, S. Weiss, E. Charbon, X. Intes, "NIR fluorescence lifetime macroscopic imaging with a time-gated SPAD camera", Proceedings of SPIE 11965 (2022) 1196507, `doi: 10.1117/12.2607833 <https://doi.org/10.1117/12.2607833>`_

.. [XM23] X. Michalet, A. Ulku, M. A. Wayne, C. Bruschini, S. Weiss, E. Charbon, "NIR fluorescence lifetime macroscopic imaging with a novel time-gated SPAD camera", Proceedings of SPIE 12384 (2023) 1238409, `doi: 10.1117/12.2649227 <https://doi.org/10.1117/12.2649227>`_

.. [DR24] D. Roy, X. Michalet, E. W. Miller, S. Weiss, "Towards optical measurements of membrane potential values in Bacillus subtilis using fluorescence lifetime", Biophysical Reports 5 (2025) 100196, `doi: 10.1016/j.bpr.2025.1001960 <https://doi.org/10.1016/j.bpr.2025.100196>`_

.. [XM25] X. Michalet, "AlliGator: Open Source Fluorescence Lifetime Imaging Analysis in G", SoftwareX (2025) under review, `doi: 10.1101/2025.05.22.655640 <https://doi.org/10.1101/2025.05.22.655640>`_
