.. _alligator-python-plugins-API:

The following sections describe the different parameter types and internal 
AlliGator variables that can be passed.

AlliGator Python Plugins API v 1
++++++++++++++++++++++++++++++++

AlliGator versions: 0.63-current

Parameter Types
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
   AlliGator, Phasor Frequency, any exposed AlliGator parameter [*]_

.. [*] Requested AlliGator parameters are provided automatically to the plugin 
   function. To obtain a list of current exposed internal AlliGator parameters, 
   use the *Send* button in the **Settings:Plugins** panel. This will send a 
   copy of that list to the Clipboard, together with the current parameter 
   values.

A list of exposed parameters with their default values can be found 
:ref:`here <alligator-internal-parameters>`.

Check the *Parameter Names only* checkbox in the **Settings:Plugins** panel to 
get a list of exposed internal AlliGator parameters without their 
current value.

AlliGator Python Plugin Data Types
----------------------------------

The different data types are declared in the ``alligator.py`` script found in the 
*Python Plugins* folder, reproduced below:

.. code-block::

    # AlliGator Python Plugin Definitions
    # Author: X. Michalet
    # Last modified: 2026-02-18

    ### AlliGator Python Plugin API Version = 1 ###

    # makes sure the path to AlliGator Plugins is known to Python

    import os
    import sys

    def define_plugin_path():

        if not (os.getenv('LOCALAPPDATA')+'/AlliGator/Python Plugins' in os.environ):
            sys.path.append(os.getenv('LOCALAPPDATA')+'/AlliGator/Python Plugins')
            
        return()
        
        
    import collections
    from collections import namedtuple

    graph_plugin_data = namedtuple('graph_plugin_data',\
        'Graph_Name, Plots, Reference_Decay')

    # where 'Plots' is a list of, and 'Reference_Decay' is a, plot_plugin_data:

    plot_plugin_data = namedtuple('plot_plugin_data',\
        'Plot_Name, X_Array, Y_Array')

    # where 'X_Array' and 'Y_Array' are 1D lists of double-precision 
    # floating point numbers

    empty_plot = plot_plugin_data(Plot_Name = '', X_Array = [], Y_Array = [])

    fli_dataset_plugin_data = namedtuple('fli_dataset_plugin_data',\
        'FLI_Dataset_Name, Gate_Duration, \
        Gate_Separation, Gate_Number, X_Size, Y_Size, Image_Data_List,\
        Reference_Decay, Mask_Image, Parameter_Map')

    # where 'Image_Data_List' is a list of image_plugin_data:

    image_plugin_data = namedtuple('image_plugin_data',\
        'Image_Name, Image')

    # where 'Image' is a 2D list of single-precision floating point numbers

    # and 'Parameter_Map' is a named tuple:

    parameter_map_plugin_data = namedtuple('parameter_map_plugin_data',\
        'Parameter_Names, Parameter_Flattened_Map, Locations,\
        IRF_X,IRF_Y_Flattened_List')

    # where 'Parameter_Names' is a list of provided parameters,
    # 'Parameter_Flattened_Map' is a list of parameter lists, one parameter list
    # per valid location
    # 'Locations' is a list of namedtuple, coordinatess of the fitted decays
    # 'IRF_X' is the common time axis of al IRFs
    # 'IRF_Y_Flattened_List' is a list of IRF Intensities at the different locations
    # Note that in principle, the number of locations can be different from the
    # number of parameter lists

    empty_map = parameter_map_plugin_data(
        Parameter_Names = [],
        Parameter_Flattened_Map = [],
        Locations = [],
        IRF_X = [],
        IRF_Y_Flattened_List = [])

    location = namedtuple('location', 'X, Y')

