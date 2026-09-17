# FLI_Dataset_to_Parameter_Map_Plugin_Example.py
# Example AlliGator FLI Dataset Menu Python Plugin
# Tested with AlliGator version 1.07
# Author: X. Michalet
# Last modified: 2026-07-29

# The following (triple) comment is needed to specify the AlliGator Python 
# Plugin API version number to use

### AlliGator Python Plugin API Version = 1.1 ###

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
import alligatorFLI_1_1

# the following module is used in this plugin

import numpy as np

def Very_Simple_Average_Lifetime_Map(
        plugin_data_in, params_in_json, addtl_params_out_json_list):
        
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
    ### Low Count Pixels Rejection Options: AlliGator
    # the reference decay is part of the input plugin_data_in
    ### End of AlliGator Input Parameters Definitions ###

    # The following (triple commented) section is mandatory to know which
    # type of output this function returns and which AlliGator
    # object they are destined to

    ### AlliGator Output Value Type & Destination ###
    ### Parameter Map:Parameter Map
    ### End of AlliGator Output Value Type & Destination ###

    # decode the plugin data
    
    fli_dataset_data_in = plugin_data_in.FLI_Dataset_Plugin_Data
    fli_dataset_name = fli_dataset_data_in.FLI_Dataset_Name
    gate_duration = fli_dataset_data_in.Gate_Duration
    gate_separation = fli_dataset_data_in.Gate_Separation
    gate_number = fli_dataset_data_in.Gate_Number
    size_x = fli_dataset_data_in.X_Size
    size_y = fli_dataset_data_in.Y_Size
    images = fli_dataset_data_in.Image_Data_List
    # mask = fli_dataset_data_in.Mask_Image     # unused in this function

    graph_data_in = plugin_data_in.Graph_Plugin_Data
    ref_decay = graph_data_in.Reference_Decay

    # decode the parameter string

    params = json.loads(params_in_json)
    low_count_pixel_options = params['Low Count Pixels Rejection Options']
    
    # print(str(low_count_pixel_options))
    
    reject_low_count_pixels = low_count_pixel_options['Reject Low Count Pixels']
    background_low_threshold_factor = low_count_pixel_options['Background Low Threshold Factor']
    fixed_low_background_threshold = low_count_pixel_options['Fixed Low Background Threshold']
    low_percentile = low_count_pixel_options['Low Percentile']
    
    # !!! in this example, we ignore background_low_threshold_factor and
    # !!! low_percentile as they require an histogram analysis of the sun image
    # !!! we only use the fixed_low_background_threshold (if selected)
    
    if not reject_low_count_pixels: fixed_low_background_threshold = 0.0
    
    # print('reject_low_count_pixel = '+str(reject_low_count_pixels))
    # print('fixed_low_background_threshold = '+str(fixed_low_background_threshold))
    
    # process gate series: calculate a pseudo average lifetime as
    # <tau> = sum((i - i0)*y_i)*dt/sum(y_i) where i0 is the peak location
    
    dt = gate_separation*1E9                              # step in ns
    sum = np.zeros((size_y,size_x),dtype=np.float32)      # init sum image
    integral = np.zeros((size_y,size_x),dtype=np.float32) # init integral image
    decay_sum = np.zeros(gate_number,dtype=np.float32)    # init decay sum
    mean_t = np.empty((size_y,size_x),dtype=np.float32)   # init mean t image

    # find location of maximum assuming there is no offset between pixels
    
    for i in range(gate_number):
        decay_sum[i] = np.asarray(images[i].Image).sum()
    i0 = decay_sum.argmax()
    
    # Note: alternatively, the Sum_Image data of the FLI Dataset Data structure
    # could be used
    
    # compute integrals of t*y and y
    
    for i in range(gate_number):
        gate = np.asarray(images[i].Image)
        np.add(sum, gate, out = sum)
        time = (i-i0)*dt
        np.add(integral, gate*time, out = integral)
        
    # replace sun values lower than threshold by nan
    
    sum[sum < fixed_low_background_threshold] = np.nan
    
    # compute mean tau

    mean_t = np.divide(integral, sum)
    
    # building the parameter map
    
    # not all parameters need to be provided, in which case only the names
    # of the provided parameters are needed

    parameter_names = ['A_1','<tau>_a']
    
    # copying IRFs from input data
    
    irf_x = ref_decay.X_Array
    irf_y = ref_decay.Y_Array       # if there is a single IRF
                                    # otherwise provide one irf_y per location

    # fill the two flattened maps
 
    irf_locations = []              # will be filled with locations
    parameter_map = []              # will be filled with parameter values
    for i in range(size_x):
        for j in range (size_y):
            irf_locations.append(alligatorFLI_1_1.location(X = i, Y = j))
            parameter_map.append([i, j, sum[j, i],mean_t[j, i]])
    
    # print(str(parameter_map[:1000]))
    
    # packaging everything in the output format
    
    simple_map_data = alligatorFLI_1_1.parameter_map_plugin_data(
        Parameter_Names = parameter_names,
        Parameter_Flattened_Map = parameter_map,
        Locations = irf_locations,
        IRF_X = irf_x,
        IRF_Y_Flattened_List = [irf_y],
        X_Resolution = size_x,
        Y_Resolution = size_y
    )
    
    plugin_data_out = alligatorFLI_1_1.plugin_data(
        Image_Plugin_Data =alligatorFLI_1_1.empty_image,
        Graph_Plugin_Data = alligatorFLI_1_1.empty_graph,
        Parameter_Map_Plugin_Data = simple_map_data,
        FLI_Dataset_Plugin_Data = alligatorFLI_1_1.empty_fli_dataset)
    
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
    
    # return the plugin data containing the parameter map and the mask
    
    return(plugin_data_out)