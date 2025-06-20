# FLI_Dataset_Plugin_Example.py
# Example AlliGator FLI Dataset Menu Python Plugin
# Tested with AlliGator version 1.02
# Author: X. Michalet
# Last modified: 2025-06-19

# The following (triple) comment is needed to specify the AlliGator Python 
# Plugin API version number to use

### AlliGator Python Plugin API Version = 1 ###

# The following (triple) comment is needed to tell AlliGator where to
# insert the plugin function(s) as menu item(s)
# the syntax after the AlliGatorTarget = keyword is:
# Window/Type_of_Destination/Destination
# where 'Window' is the target AlliGator window, 'Type_of_Destination' is
# 'Object' or 'Menu', and 'Destination' is the name of the object,
# or the menu item under which to insert the script's functions as
# 'script_name>>plugin function'

### AlliGatorTarget = AlliGator/Menu/FLI Dataset ###

# The following modules are needed to interpret incoming data and send outputs

import json
import alligator

# the following module is used in this plugin

import numpy as np

def Peak_Intensity_Above_Threshold_Mask(
        fli_dataset_data_in, params_in_json, addtl_params_out_json_list):
        
    """Peak Intensity Above Threshold Mask

    Expects one float parameter (th: float64)
    from the calling VI and processes the incoming Dataset as follows:
    max of all gates -> max
    if max > th, mask = 1, else mask = 0
    The resulting processed mask image is returned to AlliGator
    """
    # The following (triple) comment indicates that this function is a plugin
    # This is to distinguish it from accessory functions that should
    # not be imported in AlliGator's menus

    ### IsAlliGatorPythonPlugin ###

    # The following (triple commented) section describes which
    # additional parameters are required for that function.
    # If no parameter is needed this section can be ignored

    ### AlliGator Input Parameters Definitions ###
    ### th:float64            # peak intensity threshold parameter
    ### End of AlliGator Input Parameters Definitions ###

    # The following (triple commented) section is mandatory to know which
    # type of output this function returns and which AlliGator
    # object they are destined to

    ### AlliGator Output Value Type & Destination ###
    ### Mask Image:Source Image # comments are OK.

    ### End of AlliGator Output Value Type & Destination ###

    # decode the dataset
    
    fli_dataset_name = fli_dataset_data_in.FLI_Dataset_Name
    gate_duration = fli_dataset_data_in.Gate_Duration
    gate_separation = fli_dataset_data_in.Gate_Separation
    gate_number = fli_dataset_data_in.Gate_Number
    size_x = fli_dataset_data_in.X_Size
    size_y = fli_dataset_data_in.Y_Size
    images = fli_dataset_data_in.Image_Data_List

    # decode the parameter string

    params = json.loads(params_in_json)
    threshold = params['th']
    
    # process gate series
    
    max = np.zeros((size_y,size_x),dtype=np.float32)    # init max image
    for i in range(gate_number):
        gate = np.asarray(images[i].Image)
        max = np.maximum(max, gate, out = max)
    mask = (max > threshold).astype('uint16')  # set values > th in max to 1
                                               # set values <= th to 0
    mask_as_list = mask.tolist() # LabVIEW only accepts list as array output

    fli_dataset_data_out = alligator.fli_dataset_plugin_data(
        FLI_Dataset_Name = '',
        Gate_Duration = 0,
        Gate_Separation = 0,
        Gate_Number = 1,
        X_Size = size_x,
        Y_Size = size_y,
        Image_Data_List = [],
        Reference_Decay = alligator.empty_plot,
        Mask_Image = mask_as_list,
        Parameter_Map = alligator.empty_map
    )
    
    # We can send back information on the function outcome
    # and can also set AlliGator Parameters
    # all this packaged in a dictionary, converted to json and
    # appended to the (generally) empty string list
    # addtl_params_out_json_list
    # Note: space and case are irrelevant in the item names

    info_out_dict = {
    "Notebook Message" : "Mask image from peak intensity above threshold",
    "Exception Type" : "None", # could also be "Warning" or "Error"
    "Exception Message" : "", # provide verbose information for error
    }
    
    # conversion to JSON string and string is appended to the incoming
    # addtl_params_out_json_list (which is empty in this example)
    # Note that AlliGator will ignore everything but the last string in the list
    
    addtl_params_out_json_list.append(json.dumps(info_out_dict))
    
    # return the Mask Image to AlliGator
    
    return(fli_dataset_data_out)