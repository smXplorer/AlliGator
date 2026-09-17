########################################
# AlliGator Python Plugin Definitions  #
# Author: X. Michalet                  #
# Last modified: 2026-09-15            #
########################################
#                                      #
#     DO NOT MODIFY THIS FILE !!!      #
#                                      #
########################################

### AlliGator Python Plugin API Version = 1.1 ###

import collections
from collections import namedtuple

###############################################################################
# Object Definitions, in order of increasing complexity (and interdependence)
###############################################################################

###############################################################################
# Location
###############################################################################

location = namedtuple('location', 'X, Y')

###############################################################################
# Plot
###############################################################################

plot_plugin_data = namedtuple('plot_plugin_data',\
    'Plot_Name, X_Array, Y_Array')

# where 'X_Array' and 'Y_Array' are 1D lists of double-precision 
# floating point numbers

empty_plot = plot_plugin_data(Plot_Name = '', X_Array = [], Y_Array = [])

###############################################################################
# Graph: contains several plots (not necessarily all plots of a source graph)
###############################################################################

graph_plugin_data = namedtuple('graph_plugin_data',\
    'Graph_Name, Plots, Reference_Decay')

# where 'Plots' is a list of, and 'Reference_Decay' is a single,
# plot_plugin_data object

empty_graph = graph_plugin_data(
    Graph_Name = '',
    Plots = [],
    Reference_Decay = empty_plot)

###############################################################################
# Image
###############################################################################

image_plugin_data = namedtuple('image_plugin_data',\
    'Image_Name, Image')

# where 'Image' is a 2D list of single-precision floating point numbers

empty_image = image_plugin_data(Image_Name = '', Image = [])

###############################################################################
# Parameter Map
###############################################################################

parameter_map_plugin_data = namedtuple('parameter_map_plugin_data',\
    'Parameter_Names, Parameter_Flattened_Map, Locations,\
    IRF_X,IRF_Y_Flattened_List,X_Resolution, Y_Resolution')

# where 'Parameter_Names' is a list of provided parameters,
# 'Parameter_Flattened_Map' is a list of parameter lists, one parameter list
# per valid location
# 'Locations' is a list of namedtuple, coordinates of the fitted decays
# 'IRF_X' is the common time axis of all IRFs
# 'IRF_Y_Flattened_List' is a list of IRF Intensities at the different locations
# Note that in principle, the number of locations can be different from the
# number of parameter lists

empty_parameter_map = parameter_map_plugin_data(
    Parameter_Names = [],
    Parameter_Flattened_Map = [],
    Locations = [],
    IRF_X = [],
    IRF_Y_Flattened_List = [],
    X_Resolution = 0,
    Y_Resolution = 0)

###############################################################################
# FLI Dataset
###############################################################################

fli_dataset_plugin_data = namedtuple('fli_dataset_plugin_data',\
    'FLI_Dataset_Name, Gate_Duration, Gate_Separation, Gate_Number,\
    X_Size, Y_Size, Image_Data_List, Mask_Image, Sum_Image, Max_Image,\
    Min_Image')
   
empty_fli_dataset = fli_dataset_plugin_data(
    FLI_Dataset_Name = '',      # string
    Gate_Duration = 0,          # DBL
    Gate_Separation = 0,        # DBL
    Gate_Number = 0,            # I32
    X_Size = 0,                 # I32
    Y_Size = 0,                 # I32
    Image_Data_List = [],       # list of SGL 2D arrays
    Mask_Image = [],            # U16 2D array
    Sum_Image = [],             # SGL 2D array
    Max_Image = [],             # SGL 2D array
    Min_Image = [])             # SGL 2D array

###############################################################################
# Python Plugin Data
###############################################################################

plugin_data = namedtuple('plugin_data',\
    'Image_Plugin_Data, Graph_Plugin_Data, Parameter_Map_Plugin_Data,\
    FLI_Dataset_Plugin_Data')

# where the different objects are:
# Image_Plugin_Data: of type image_plugin_data
# Graph_Plugin_Data: of type graph_plugin_data
# Parameter_Map_Plugin_Data: of type parameter_map_plugin_data
# FLI_Dataset_Plugin_Data: of type fli_dataset_plugin_data

empty_plugin_data = plugin_data(
    Image_Plugin_Data = empty_image,
    Graph_Plugin_Data = empty_graph,
    Parameter_Map_Plugin_Data = empty_parameter_map,
    FLI_Dataset_Plugin_Data = empty_fli_dataset)
