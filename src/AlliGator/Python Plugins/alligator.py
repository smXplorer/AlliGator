# AlliGator Python Plugin Definitions
# Author: X. Michalet
# Last modified: 2024-10-18

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
    'Graph_Name, Plots, Reference_Decay'

)

# where 'Plots' is a list of, and 'Reference_Decay' is a, plot_plugin_data:

plot_plugin_data = namedtuple('plot_plugin_data',\
    'Plot_Name, X_Array, Y_Array'
)

# where 'X_Array' and 'Y_Array' are 1D lists of double-precision 
# floating point numbers

empty_plot = plot_plugin_data(Plot_Name = '', X_Array = [], Y_Array = [])

fli_dataset_plugin_data = namedtuple('fli_dataset_plugin_data',\
    'FLI_Dataset_Name, Gate_Duration, \
    Gate_Separation, Gate_Number, X_Size, Y_Size, Image_Data_List,\
    Reference_Decay, Mask_Image, Parameter_Map'
)

# where 'Image_Data_List' is a list of image_plugin_data:

image_plugin_data = namedtuple('image_plugin_data',\
    'Image_Name, Image'
)

# where 'Image' is a 2D list of single-precision floating point numbers

# and 'Parameter_Map' is a named tuple:

parameter_map_plugin_data = namedtuple('parameter_map_plugin_data',\
    'Parameter_Names, Parameter_Flattened_Map, Locations,\
    IRF_X,IRF_Y_Flattened_List'
)

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
    IRF_Y_Flattened_List = []
)

location = namedtuple('location', 'X, Y')
