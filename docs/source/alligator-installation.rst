.. _alligator-installation:

AlliGator Installation
======================

This section describes requirements and procedures for installing the standalone 
application (several copies of which can be launched in parallel). A development 
LabVIEW installation is not needed, but if present (and of the correct version, 
*i.e*. 2021 SP1), will dispense of having to install the runtime engine 
described below. Likewise, if a development version of the Vision Development 
Module (2021) is installed, the VDM RTE installation step can be skipped.

System Requirements
+++++++++++++++++++

This software will only run on Microsoft Windows 10 64 bit.
Some of the functions used by the software support parallelism, therefore a
multiprocessor and/or multicore computer is recommended (this statement is not 
as dated as it sounds, as virtual machines offer the choice of core number).
Since time-gated image datasets tend to be large, and many analysis steps 
involve processing all time-gate images, it is preferable to have as much RAM 
as possible available. 16 GB or more are recommended.

Download the Installer(s)
+++++++++++++++++++++++++

3 pieces of software need to be present on your computer for AlliGator to run 
properly:

  * AlliGator
  * LabVIEW Run-time Engine (RTE)
  * Vision Development Module (VDM) RTE

Follow the instructions below to make sure you install the correct versions of 
each. Do not hesitate to post a support request on the `AlliGator Support Google 
Group <https://groups.google.com/u/1/g/alligator-software-support>`_ to ask for 
help or advice. You only need to install the LabVIEW and VDM RTE once. Note that 
if you have a development version of both LabVIEW 2021 SP1 and VDM 2021, there 
is no need to install these RTE.

AlliGator Installer
-------------------

Find and download the latest installer zip archive in the `installer/latest 
<https://github.com/smXplorer/AlliGator/tree/main/installer/latest>`_ folder 
of the AlliGator GitHub repository.

Installers for previous versions can be found in the `installer 
<https://github.com/smXplorer/AlliGator/tree/main/installer>`_ folder and can be 
run to overwrite a newer version containing a bug or to replicate published 
analysis performed with an older version.

Note that older AlliGator versions may require older LabVIEW and VDM RTE, as 
explained in the :ref:`AlliGator and LabVIEW versions <alligator-labview-versions>` 
section below.


LabVIEW and Vision Development Module RTE
-----------------------------------------

The AlliGator installer only installs the software and its dependent files, but 
won't result in a functional executable unless you have the LabVIEW 2021 SP1 64 
bit Run-Time Engine (RTE) installed on your machine, as well as the Vision 
Development Module (VDM) 2021 Run-time Engine.

The LabVIEW RTE installer is available for free from National Instruments at 
<https://www.ni.com/en/support/downloads/software-products/download.labview-runtime.html#443841>


Although the VDM RTE is free to download at <https://www.ni.com/en/support/downloads/software-products/download.vision-development-module-runtime.html#409837>, 
it requires a license to be used (asked for during installation). As explained 
`here <https://www.ni.com/en/support/documentation/supplemental/18/licensing-national-instruments-vision-software.html>`_ a trial license can be requested from Natioanl Instruments/Emerson, 
but it will expire after a one week trial period. If you have a license for a 
different version of VDM, it will work. As of 2/2024, an academic license costs 
$407.40 ($582 for non-academic users).

Installation Instructions
-------------------------

Once the LabVIEW RTE and then the VDM RTE are installed (this only needs to be 
done once), run the ``install.exe`` file in the AlliGator installer zip file 
(there is no need to unzip the installer). The default installation folder is in 
the logged Windows user's personal folder, therefore no Administrator right is 
needed.

There is no need to uninstall a previous version to install a new one (which can 
be done from within AlliGator using the ``Check for Update`` item of the Help 
menu).

.. _alligator-labview-versions:

AlliGator and LabVIEW Versions
------------------------------

AlliGator is developed using the graphical programming language LabVIEW and uses 
the Vision Development Module (VDM) toolkit for some image handling and analysis 
functions. The software therefore requires the LabVIEW runtime engine (RTE) and 
the VDM RTE corresponding to the version it was developed with.

Note that for AlliGator versions anterior to 0.80, version 1.8.18 of the HDF5 
library needs to be installed separately, as explained in section 
:ref:`HDF5 library installation <HDF5-library-installation>` below.

Over the years, different LabVIEW versions have been used and therefore, 
different versions of AlliGator require different versions of the LabVIEW and 
VDM RTE, as explained below.

* LabVIEW 2021 SP1 64 bit for version 0.51 and above
    * LabVIEW RTE: <https://www.ni.com/en/support/downloads/software-products/download.labview-runtime.html#443841>
    * VDM RTE: <https://www.ni.com/en/support/downloads/software-products/download.vision-development-module-runtime.html#409837>
    
* LabVIEW 2019 SP1 64 bit for version 0.21 to 0.50
    * LabVIEW RTE: https://www.ni.com/en/support/downloads/software-products/download.labview.html#348045>
    * VDM RTE:<https://www.ni.com/en-us/support/downloads/software-products/download.vision-development-module.html#329029>

* LabVIEW 2018 SP1 64 bit for version 0.15 to 0.20.4
    * LabVIEW RTE: <https://www.ni.com/en-us/support/downloads/software-products/download.labview.html#309628>
    * VDM RTE: <https://www.ni.com/en-us/support/downloads/software-products/download.vision-development-module.html#306495>

* LabVIEW 2017 SP1 64 bit for version 0.9.11 to 0.15
    * LabVIEW RTE: <https://www.ni.com/en-us/support/downloads/software-products/download.labview.html#310821>
    * VDM RTE: <https://www.ni.com/en-us/support/downloads/software-products/download.vision-development-module.html#306485>

* LabVIEW 2016 64 bit for versions prior to 0.9.11
    * LabVIEW RTE: <https://www.ni.com/en-us/support/downloads/software-products/download.labview.html#310817>
    * LabVIEW VDM RTE: <https://www.ni.com/en-us/support/downloads/software-products/download.vision-development-module.html#306484>

Several versions of the RTE can be installed concurrently on the same machine, 
but since they are hefty, it is possible to uninstall the unused versions to 
save space.

Uninstalling AlliGator does not uninstall the corresponding RTE version, 
therefore it is only necessary to install the required RTE once.

Note that if you have the correct *LabVIEW development environment* installed on 
your machine, there is no need to install the RTE again, as it will already be 
available.

.. _HDF5-library-installation:

HDF5 Library Installation
-------------------------

In order to be able to save and load HDF5 files introduced in version 0.16, HDF5 
library version 1.8.18 needs to be installed *for AlliGator versions anterior to
version 0.80*. AlliGator 0.80 and above include the HDF5 library (version 
2.15.0.149) in the installer, therefore this step can be ignored.

The free HDF5 library installer archive can be found here: <https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8/hdf5-1.8.18/bin/windows/hdf5-1.8.18-win64-vs2013-shared.zip>

