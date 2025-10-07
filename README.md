![AlliGator Logo](/docs/source/images/AlliGator-Picture.png)
# AlliGator
A LabVIEW software for Fluorescence lifetime imaging dataset analysis

*See this open access SoftwareX article* (https://doi.org/10.1016/j.softx.2025.102255) 
*for an overview of the software*

This repository contains both *source code* and *installer for the standalone 
executable*.

## Standalone executable installer

Instructions on how to install AlliGator can be found in the *AlliGator Installation* 
page of the online manual: https://alligator-distribution.readthedocs.io/en/latest/alligator-installation.html

For the latest standalone AlliGator software installer, check the 
https://github.com/smXplorer/AlliGator/tree/main/installer/latest folder. This 
executable requires the LabVIEW 2021 SP1 runtime (free) and Vision Development 
Module 2021 runtime (to be purchased from Emerson/National Instruments).

The latest online manual can be found at https://alligator-distribution.readthedocs.io, 
where a PDF version can also be found.

For a legacy AlliGator manual, check the older AlliGator website backed-up on 
the Internet Archive at https://web.archive.org/web/20201028034436/https://sites.google.com/a/g.ucla.edu/alligator/manual
(Note that the link to a PDF version of the manual on this archived website is dead). 

New standalone version releases and changelogs are posted on the AlliGator 
Google Group site at https://groups.google.com/g/alligator-software-support

The version history page can be found at https://alligator-distribution.readthedocs.io/en/latest/alligator-version-history.html

## LabVIEW 2021 SP1 source code (Windows 64 bit compatible)

The LabVIEW 2021 SP1 source code can be found in the *src* directory.

AlliGator depends on the following packages:

in vi.lib: 
- Vision Development Module (requires a license from Emerson/National Instruments)
- IlluminatedG/IG AutoComplete (free)
- JDP Science/Common Utilities, JSONText (free)

in vi.lib/addons:
- Advanced Signal Processing Toolkit/Time Series Analysis, Time Frequency 
Analysis, Wavelet Analysis (requires a license from Emerson/National Instruments)
- Hierarchical Data Format (HDF5) (formerly known as h5labview2) (free)

in user.lib:
- OpenG Toolkit/array, error, file, lvdata, lvzip, md5, string, time, 
  variantconfig (free)
- Hooovahh/Array VIMs (free)
- MGI Graph (free)


The free packages can be found on VIPM.io (https://www.vipm.io/) or using the 
free VIPM (VI package Manager) distributed by JKI 
(https://www.vipm.io/download/).

To use the source code, open the AlliGator.lvproj project in LabVIEW and look 
for the *AlliGator Launcher.vi* VI in *AlliGator GUI.lvlib* in the *VIs* folder 
of the project. This is the top-level VI that needs to be run to start 
AlliGator. Running AlliGator.vi directly will fail, as some preparatory steps 
are handled by AlliGator Launcher.vi.

## Source code documentation

A list of Virtual Instruments (VIs) included in the distribution, as well as 
their brief description by library can be found in the *src-docs* directory, 
and can be accessed by opening the Project-Documentation.html or the 
Project-Documentation.pdf files.