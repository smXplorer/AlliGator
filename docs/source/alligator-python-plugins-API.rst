.. _alligator-python-plugins-API:

AlliGator Python Plugins API v 0.1
++++++++++++++++++++++++++++++++++

AlliGator versions: 0.63-current

.. toctree::
   alligator-internal-parameters

parameter types
---------------
The following input parameter types are supported:

.. csv-table::
   :header: "Type", "Example", "Description"

   U8, 1, unsigned byte
   U16, 1, unsigned short integer
   U32, 1, unsigned long integer
   I8, -1, signed byte
   I16, -1, signed short integer
   I32, -1, signed long integer
   float32, 1.0, single-precision floating point number
   float64, 1.0, double-precision floating point number
   string, a string, string
   path, "C:\\Desktop\\test.txt", file or folder path
   boolean, True, boolean: True or False
   AlliGator, Phasor Frequency, any exposed AlliGator parameter (*)

(*) Requested AlliGator parameters are provided automatically to the plugin 
function. To obtain a list of current exposed internal AlliGator parameters, 
use the *Send* button in the **Settings:Plugins** panel. This will send a copy 
of that list to the Clipboard, together with the current parameter values.

A list of exposed parameters with their default values can be found 
:ref:`here <alligator-internal-parameters>`.

Check the *Parameter Names only* checkbox in the **Settings:Plugins** panel to 
get a list of exposed internal AlliGator parameters without their 
current value.

