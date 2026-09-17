# Sliced_Decay_Variation_Analysis.py
# Analysis of multiple ROI IRFs by intensity slice
# Tested with AlliGator version 1.07
# Author: X. Michalet
# Last modified: 2026-09-16

# The following (triple) comment is needed to specify the AlliGator Python 
# Plugin API version number to use

### AlliGator Python Plugin API Version = 1.1 ###

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
import alligatorFLI_1_1

# the following modules are used in this plugin

import numpy as np
import math

def Sliced_Decay_Variation_Analysis(
        plugin_data_in, params_in_json, addtl_params_out_json_list):
        
    """
    Expects 8 parameters to define the intensity slices used during analysis,
    entered in a dialog window opening when the function is called:
    
      Min Intensity (MinI: float64), if NaN, the min intensity value is used.
      Max Intensity (MaxI: float64), if NaN, the max intensity value is used.
      # Slices (NSlices: int32), is the number of slices into which to divide 
        the range [MinI, MaxI].
      Slice Width (SliceW: float64), is the size of each slice (max intensity 
        minus min intensity of each slice, except possibly for the last one.
      # Elements (NElts: int32), is the number of elements per slice, except 
        possibly for the last one.
      Parameter Choice (Choice: int32), is a number between 1 and 3 (rounded 
        to the closest valid value) specifying whether to define slices by the
        # Slices (1), Slice Width (2) or # Elements (3). 
      Min Data Points per Slice (NMin: int32), is a parameter allowing to 
        ignore slices with too few data points.
      Bin Location (BinLoc: int32), a value between 0 and 3, specify how to 
        define the slice representative intensity (0: Left, 1: Center, 2: Mean, 
        3: Right), where Left (resp. Right) represents the lower (resp. upper) 
        boundary of the slice, Center represents the middle of the slice and 
        Mean is the average intensity in the slice.
      
    as well as an optional mask and processes the incoming FLI Dataset as
    follows:
    
    The intensities of all ROIs are sorted into consecutive slices based on 
    the input parameters, in analogy to the Compute Sliced Mean, SDV and CV 
    Plots function of the Lifetimes & Other Parameters Graph.
    
    The resulting average decay followed by the decay standard deviation for 
    each slice, are returned to AlliGator's Decay Graph, together with a 
    summary of the analysis in the Notebook.
    """
    # The following (triple) comment indicates that this function is a plugin
    # This is to distinguish it from accessory functions that should
    # not be imported in AlliGator's menus

    ### IsAlliGatorPythonPlugin ###

    # The following (triple commented) section describes which
    # additional parameters are required for that function.
    # If no parameter is needed this section can be ignored

    ### AlliGator Input Parameters Definitions ###
    ### MinI:float64:NaN        # min intensity value
    ### MaxI:float64:NaN        # max intensity value
    ### NSlices:I32:10          # number of slices
    ### SliceW:float64          # size of each slice
    ### NElts:float64           # number of elements per slice (unsupported)
    ### Choice:I32:1            # which of the previous 3 parameters is used (1-3)
    ### NMin:I32:10             # ignore slices with less than NMin data points
    ### End of AlliGator Input Parameters Definitions ###

    # UPer:float64:100  # reject possible high intensity outliers (100: no 
    # outlier is rejected, unsupported)
    # LPer:float64:0    # reject possible low intensity outliers (0: no outlier 
    # is rejected, unsupported)

    # The following (triple commented) section is mandatory to know which
    # type of output this function returns and which AlliGator
    # object they are destined to

    ### AlliGator Output Value Type & Destination ###
    ### Plots:Decay Graph
    ### End of AlliGator Output Value Type & Destination ###

    # decode the dataset
    
    fli_dataset_data_in = plugin_data_in.FLI_Dataset_Plugin_Data
    fli_dataset_name = fli_dataset_data_in.FLI_Dataset_Name
    gate_duration = fli_dataset_data_in.Gate_Duration
    gate_separation = fli_dataset_data_in.Gate_Separation
    gate_number = fli_dataset_data_in.Gate_Number
    size_x = fli_dataset_data_in.X_Size
    size_y = fli_dataset_data_in.Y_Size
    gate_images = fli_dataset_data_in.Image_Data_List
    mask_image = fli_dataset_data_in.Mask_Image
    intensity_image = fli_dataset_data_in.Sum_Image

    # decode the parameter string

    params = json.loads(params_in_json)
    MinI = params['MinI']
    MaxI = params['MaxI']
    n_slices = max(1, params['NSlices'])
    slice_width = max(1, params['SliceW'])
    n_elts = max(1,params['NElts'])
    Choice = params['Choice']
    NMin = max(1,params['NMin'])

    # computes slice boundaries, emulating AlliGator Sliced Analysis Initialization.vi
    
    intensity_array = np.reshape(np.asarray(intensity_image),size_x*size_y)
    if len(mask_image) == 0:
        mask_message = 'no mask provided'
        mask_on = 0     # no mask provided means all pixels are used
        sorted_indices = np.argsort(intensity_array)  # gets indices of sorted intensities
        sorted_intensity_array = np.sort(intensity_array)
    else:
        mask_message = 'mask provided'
        mask_on = 1
        mask_array = np.reshape(np.asarray(mask_image),size_x*size_y)
        idx = np.argsort(intensity_array[mask_array == 1]).astype(int)
        sorted_indices = np.flatnonzero(mask_array == 1)[idx].astype(int)
        # sorted_indices are the indices in the original intensity_array, 
        # of intensities where mask_array is non zero
        
        sorted_intensity_array = np.sort(intensity_array[mask_array == 1])
        
    sorted_intensity_array_min = sorted_intensity_array[0]      # min intensity
    sorted_intensity_array_max = sorted_intensity_array[-1]     # max intensity
        
    # defines min and max boundaries
    
    if not math.isfinite(MinI):     # checks for NaN and +/- Inf
        min_I = sorted_intensity_array_min
    else:
        min_I = MinI
        
    if not math.isfinite(MaxI):     # checks for NaN and +/- Inf
        max_I = sorted_intensity_array_max
    else:
        max_I = MaxI
    
    if Choice == 1:     # fixed number of slices
        choice_string = 'Choice: number of slices = '+str(n_slices)
        # compute slice width
        slice_width = (max_I-min_I)/n_slices
        
    elif Choice == 2:   # fixed slice size
        choice_string = 'Choice: slice width = '+str(slice_width)
        # compute slice number
        n_slices = math.ceil((max_I - min_I)/slice_width)
        
    elif Choice == 3:   # fixed number of elements per slice
        choice_string = 'Choice: number of elements per slice = '
        # This is an overestimation of the number of slices:
        n_slices = math.ceil(len(sorted_intensity_array)/n_elts)
        
    else:   # unsupported case: returns an empty structure
        plugin_data_out = alligatorFLI_1_1.empty_plugin_data
        # set the output message to explain the error
        info_out_dict = {
        "Notebook Message" : "Sliced IRF Variation Analysis",
        "Exception Type" : "Error", # could also be "Warning" or "Error"
        "Exception Message" : "Incorrect Choice value (should be 1, 2 or 3)"
        }
        addtl_params_out_json_list.append(json.dumps(info_out_dict))
        return(plugin_data_out)
        
    actual_n_slices = 0    # we will count valid slices
    
    # Defining the slice average intensity, intermediate sum decays, decay 
    # squares and slices' number of elements
    
    average_intensity = np.zeros(n_slices,dtype=np.float32)
    decay_numbers= np.zeros((n_slices),dtype=np.float32)
    
    # defining the final 2D arrays (also used for intermediate quantities)
    
    decay_averages = np.zeros((n_slices,gate_number),dtype=np.float32)
    decay_SDVs= np.zeros((n_slices,gate_number),dtype=np.float32)
    
    # defining the decay time axis
    
    time_axis = np.linspace(0, gate_number*gate_separation*1E9,gate_number,\
        endpoint=False).tolist()
    
    # We first treat cases 1 & 2
    
#    print('Length of sorted intensity array: '+str(len(sorted_intensity_array)))
    
    valid_pixels = 0
    if Choice <= 2:     # Choice == 1 or 2: fixed slice width
        for k in range(len(sorted_intensity_array)):    # loops on valid pixels
            # determines the slice index corresponding to the intensity
            slice_index = math.floor((sorted_intensity_array[k]-min_I)/slice_width)
            
            # slice_index_max = max(slice_index_max, slice_index)
            # slice_index_min = min(slice_index_min, slice_index)
            
            if slice_index >= 0 and slice_index < n_slices:
                # using the pixel index to get back to the pixel coordinates
                j = np.floor(sorted_indices[k]/size_x).astype(int) # vertical coordinate
                i = np.float64(sorted_indices[k] - j*size_x).astype(int)   # horizontal coordinate
                if i>=0 and i<size_x and j>=0 and j<size_y:  # valid pixel coordinates
                    valid_pixels += 1
                    # increments the slice content and average intensity array
                    decay_numbers[slice_index] += 1
                    average_intensity[slice_index] += sorted_intensity_array[k]
                    # adds the corresponding decay to the slice
                    for g in range(gate_number):    # loops on gates
                        gate_intensity = gate_images[g].Image[j][i]
                        decay_averages[slice_index][g] += gate_intensity
                        decay_SDVs[slice_index][g] += gate_intensity**2
            
    else:    # Choice == 3: fixed number of elements per bin
        current_slice_index = 0     # incremented as the slices fill up
        current_slice_content = 0   # incremented when a new intensity is added
        
        for k in range(len(sorted_intensity_array)):    # loops on valid pixels
            # determines the slice index corresponding to the intensity
            current_intensity = sorted_intensity_array[k]
            if current_intensity >= min_I and current_intensity <= max_I:
                # valid intensity: continue extracting data
                # if current slice is full, move to next slice
                if current_slice_content >= n_elts: # moves to next slice
                    current_slice_index += 1        # increment slice index
                    current_slice_content = 0       # set its content to 0
                # if not, use current slice
                slice_index = current_slice_index
                if slice_index >= 0 and slice_index < n_slices:
                        # using the pixel index to get back to the pixel coordinates
                        j = np.floor(sorted_indices[k]/size_x).astype(int) # vertical coordinate
                        i = np.float64(sorted_indices[k] - j*size_x).astype(int)   # horizontal coordinate
                        if i>=0 and i<size_x and j>=0 and j<size_y:  # valid pixel coordinates
                            valid_pixels += 1
                            # increments the slice content and average intensity array
                            current_slice_content += 1
                            decay_numbers[slice_index] += 1
                            average_intensity[slice_index] += sorted_intensity_array[k]
                            # adds the corresponding decay to the slice
                            for g in range(gate_number):    # loops on gates
                                gate_intensity = gate_images[g].Image[j][i]
                                decay_averages[slice_index][g] += gate_intensity
                                decay_SDVs[slice_index][g] += gate_intensity**2
                    
    # no other Choice value is expected as we have already quit the function 
    # if that is the case (see above)
    
    # computes the average and SDV decays for each slice and adds them to the
    # list of output plots
            
    plots_out = []

    # divides arrays by number of elements to obtain the final quantities
    
    for slice_index in range(n_slices):
        decay_number = decay_numbers[slice_index]
        if decay_number >= NMin:    # checks min number of elements criterion
            actual_n_slices += 1
            for g in range(gate_number):    # loops on gates
                decay_average = decay_averages[slice_index][g]/decay_number
                decay_averages[slice_index][g] = decay_average
                decay_SDV = math.sqrt(decay_SDVs[slice_index][g]/\
                    decay_number - decay_average**2)
                decay_SDVs[slice_index][g] = decay_SDV
            
            # computes slice abscissa
            average_intensity[slice_index] /= decay_number
            # use this number as part of the output plot labels
            mean_I_string = f"{average_intensity[slice_index]:.0f}"
            # builds plot outputs
            plots_out.append(alligatorFLI_1_1.plot_plugin_data(Plot_Name = \
                'Slice '+str(slice_index+1)+' (<I> = '+mean_I_string + \
                ') Average Decay', X_Array = time_axis, \
                Y_Array = decay_averages[slice_index].tolist()))
            plots_out.append(alligatorFLI_1_1.plot_plugin_data(Plot_Name = \
                'Slice '+str(slice_index+1)+' (<I> = '+mean_I_string + \
                ') Decay SDV', X_Array = time_axis,\
                Y_Array = decay_SDVs[slice_index].tolist()))
        else:   # not enough elements
            print('slice '+str(slice_index)+': '+str(decay_number))

#    print('valid pixels: '+str(valid_pixels))
    
    graph_data_out = alligatorFLI_1_1.graph_plugin_data(
        Graph_Name = 'Lifetime & Other Parameters Graph',
        Plots = plots_out,
        Reference_Decay = alligatorFLI_1_1.empty_plot)
    
    plugin_data_out = alligatorFLI_1_1.plugin_data(
        Image_Plugin_Data =alligatorFLI_1_1.empty_image,
        Graph_Plugin_Data = graph_data_out,
        Parameter_Map_Plugin_Data = alligatorFLI_1_1.empty_parameter_map,
        FLI_Dataset_Plugin_Data = alligatorFLI_1_1.empty_fli_dataset)


    # We can send back information on the function outcome
    # and can also set AlliGator Parameters
    # all this packaged in a dictionary, converted to json and
    # appended to the (generally) empty string list
    # addtl_params_out_json_list
    # Note: space and case are irrelevant in the item names
    
    if Choice == 3:
        choice_string += str(actual_n_slices)
    message = "Sliced Decays Variation Analysis options:"+\
        "\n"+mask_message+\
        "\nMin Intensity = "+str(min_I)+\
        "\nMax Intensity = "+str(max_I)+\
        "\n"+choice_string+\
        "\nMin # Elements = "+str(NMin)
    
    message += '\nslice index\t# decays\t <I>'
    
    for slice_index in range(n_slices):
        message += '\n'+str(slice_index)+'\t'+\
            f"{decay_numbers[slice_index]:.0f}"+'\t'+\
            f"{average_intensity[slice_index]:.0f}"
            
    info_out_dict = {
    "Notebook Message" : message,
    "Exception Type" : "None",  # could also be "Warning" or "Error"
    "Exception Message" : ""    # provide verbose information for error
    }
    
    # conversion to JSON string and string is appended to the incoming
    # addtl_params_out_json_list (which is empty in this example)
    # Note that AlliGator will ignore everything but the last string in the list
    
    addtl_params_out_json_list.append(json.dumps(info_out_dict))
    
    # return the mean and SDV plots to AlliGator
    
    return(plugin_data_out)