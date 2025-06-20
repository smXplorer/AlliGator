# FLI_Dataset_to_Parameter_Map_Plugin_Example.py
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
# where 'Window' is the target AlliGator window, # 'Type_of_Destination' is
# 'Object' or 'Menu', and 'Destination' is the name of the object,
# or the menu item under which to insert the script's functions as
# 'script_name>>plugin function'

### AlliGatorTarget = AlliGator/Menu/FLI Dataset ###

# The following modules are needed to interpret incoming data and send outputs

import json
import alligator

# the following module is used in this plugin

import numpy as np

def Very_Simple_Average_Lifetime_Map(
        fli_dataset_data_in, params_in_json, addtl_params_out_json_list):
        
    """Very Simple Average Lifetime Map

    Requires the reference decay and the laser period (unused)
    from the calling VI and processes the incoming Dataset as follows:
    Computes the pseudo-average lifetime (in ns)
    The resulting Parameter Map is returned to AlliGator
    """
    # The following (triple) comment indicates that this function is a plugin
    # This is to distinguish it from accessory functions that should
    # not be imported in AlliGator's menus

    ### IsAlliGatorPythonPlugin ###

    # The following (triple commented) section describes which
    # additional parameters are required for that function.
    # If no parameter is needed this section can be ignored

    ### AlliGator Input Parameters Definitions ###
    ### Laser Period: AlliGator
    # the reference decay is part of the input fli_dataset_data_in
    ### End of AlliGator Input Parameters Definitions ###

    # The following (triple commented) section is mandatory to know which
    # type of output this function returns and which AlliGator
    # object they are destined to

    ### AlliGator Output Value Type & Destination ###
    ### Decay Fit Parameters Map:Decay Fit Parameters Map Image
    ### End of AlliGator Output Value Type & Destination ###

    # decode the dataset
    
    fli_dataset_name = fli_dataset_data_in.FLI_Dataset_Name
    gate_duration = fli_dataset_data_in.Gate_Duration
    gate_separation = fli_dataset_data_in.Gate_Separation
    gate_number = fli_dataset_data_in.Gate_Number
    size_x = fli_dataset_data_in.X_Size
    size_y = fli_dataset_data_in.Y_Size
    images = fli_dataset_data_in.Image_Data_List
    ref_decay = fli_dataset_data_in.Reference_Decay
    mask = fli_dataset_data_in.Mask_Image

    # decode the parameter string

    params = json.loads(params_in_json)
    period = params['Laser Period']         # we actually don't use it...
    
    # process gate series: calculate a pseudo average lifetime as
    # <tau> = sum((i - i0)*dt*y_i)/sum(y_i) where i0 is the peak location
    
    dt = gate_separation*1E9                            # step in ns
    sum = np.zeros((size_y,size_x),dtype=np.float32)    # init sum image
    mean_t = np.zeros((size_y,size_x),dtype=np.float32) # init mean t image
    decay_sum = np.zeros(gate_number,dtype=np.float32) # init decay sum

    # Find location of maximum
    for i in range(gate_number):
        decay_sum[i] = np.asarray(images[i].Image).sum()
    i0 = decay_sum.argmax()
    
    # Compute integrals of t*y and y
    for i in range(gate_number):
        gate = np.asarray(images[i].Image)
        np.add(sum, gate, out = sum)
        np.add(mean_t, gate*(i-i0), out = mean_t)
    np.divide(mean_t*dt, sum, out = mean_t)
    
    # building the parameter map
    # init
    param_names = ['A_1','<tau>_a']
    # not all parameters need to be provided, in which case only the names
    # of the provided parameters are needed
    irf_x = ref_decay.X_Array
    irf_y = ref_decay.Y_Array       # if there is a single IRF
                                    # otherwise provide one irf_y per location
    irf_locations = []              # will be filled with locations
    param_map = []                  # will be filled with parameter values

    
    # fill the two flattened maps
    for i in range(size_x):
        for j in range (size_y):
            irf_locations.append(alligator.location(X = i, Y = j))
            param_map.append([i, j, sum[j, i],mean_t[j, i]])
    
    # packaging everything in the output format
    
    simple_map = alligator.parameter_map_plugin_data(
        Parameter_Names = param_names,
        Parameter_Flattened_Map = param_map,
        Locations = irf_locations,
        IRF_X = irf_x,
        IRF_Y_Flattened_List = [irf_y],
    )
    
    fli_dataset_data_out = alligator.fli_dataset_plugin_data(
        FLI_Dataset_Name = '',
        Gate_Duration = 0,
        Gate_Separation = 0,
        Gate_Number = 1,
        X_Size = size_x,
        Y_Size = size_y,
        Image_Data_List = [],
        Reference_Decay = alligator.empty_plot,
        Mask_Image = mask,
        Parameter_Map = simple_map
    )
    
    # We can send back information on the function outcome
    # and can also set AlliGator Parameters
    # all this packaged in a dictionary, converted to json and
    # appended to the (generally) empty string list
    # addtl_params_out_json_list
    # Note: space and case are irrelevant in the item names

    info_out_dict = {
    "Notebook Message" : 'Peak position: ' + str(i0*dt) + ' ns',
    "Exception Type" : "None", # could also be "Warning" or "Error"
    "Exception Message" : "", # provide verbose information for error
    }
    
    # conversion to JSON string and string is appended to the incoming
    # addtl_params_out_json_list (which is empty in this example)
    # Note that AlliGator will ignore everything but the last string in the list
    
    addtl_params_out_json_list.append(json.dumps(info_out_dict))
    
    # return the Mask Image to AlliGator
    
    return(fli_dataset_data_out)