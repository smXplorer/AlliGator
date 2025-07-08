# Notes on AlliGator Source Code

AlliGator is currently developed using LabVIEW 2021 SP1 64-bit on Windows 10.
Because it is using DLL calls, this prevents the source code from running on 
Windows 32 bit or other operating systems. When modifying the code, please save 
all modifications in this version for them to be testable by the original 
developer.

## File organization

AlliGator is comprised of over 4,000 VIs, saved in multiple folders outside the 
main AlliGator folder.

VIs are grouped into VI libraries (.lvlib) that can be accessed in the *VIs* 
virtual folder in the LabVIEW project. These libraries and corresponding VIs 
are physically located in the AlliGator folder of the distribution.

Other libraries not directly related to AlliGator can be found in the 
*Libraries* virtual folder of the project. The corresponding VIs are located in 
folders with the name of the library.

Some VIs in these libraries may show up as missing in the project. Because they 
are not used in AlliGator, they were not included in the automated source code 
distribution and can be safely ignored.

## How to run AlliGator

AlliGator.vi is part of the AlliGator GUI.lvlib library. However, this is not 
the VI that should be run to start the software. That role is reserved to 
AlliGator Launcher.vi, which then spawns AlliGator (and later closes it when 
the user quits AlliGator).

## How to modify AlliGator

It is recommended to open the AlliGator VIs Collection.vi VI when modifying the 
code. This VI (which cannot be run), contains all VIs of importance and all 
dynamically launched VIs, which guaranties that any modification is propagated 
throughout the whole code base (in particular type definitions).

## How to test AlliGator

A suite of test VIs can be found in the *Test Suites* folder of the project.
The top level VI is *AlliGator Test Suite*, which calls a hierarchy of 
indiviual test suites.
Associated data files can be found in the *Test Data Files* subfolder.

## Licenses

AlliGator is released under the BSD3 license, whose text can be found in the 
*Licenses* folder, together with other licenses for third-party code reused in 
the AlliGator code.