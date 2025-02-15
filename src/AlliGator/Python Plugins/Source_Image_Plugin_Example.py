# Source_Image_Plugin_Example.py
# Example AlliGator Source Image Python Plugin
# Tested with AlliGator version 0.66
# Author: X. Michalet
# Last modified: 2023-01-04

# The following (triple) comment is needed to tell AlliGator where to
# insert the plugin function(s) as menu item(s)
# the syntax after the 'AlliGatorTarget =' keyword is:
# Window/Type_of_Destination/Destination
# where 'Window' is the target AlliGator window, 'Type_of_Destination' is
# 'Object' or 'Menu', and 'Destination' is the name of the object,
# or the menu item under which to insert the script's functions as
# 'script_name>>plugin function'

### AlliGatorTarget = AlliGator/Object/Source Image ###
### AlliGatorTarget = AlliGator/Menu/Source Image ###

# The following modules are needed to interpret incoming data and send outputs

import json
import alligator

# the following module is used in this plugin

import numpy as np

def Intensity_Above_Threshold_Mask(
        image_plugin_data_in, params_in_json, addtl_params_out_json_list):
        
    """Source Image: Intensity Above Threshold Mask

    Expects one float parameter (th: float64)
    from the calling VI and processes the incoming Image as follows:
    if intensity > th, mask = 1, else mask = 0
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
    ### th:float64            # Intensity threshold parameter
    ### End of AlliGator Input Parameters Definitions ###

    # The following (triple commented) section is mandatory to know which
    # type of output this function returns and which AlliGator
    # object they are destined to

    ### AlliGator Output Value Type & Destination ###
    ### Mask Image: Source Image # empty lines as well
    ### End of AlliGator Output Value Type & Destination ###

    # get the image
    
    image = np.array(image_plugin_data_in.Image)
    size_x = image.shape[1]
    size_y = image.shape[0]
    print('x: ',size_x)
    print('y: ',size_y)

    # decode the parameter string

    params = json.loads(params_in_json)
    threshold = params['th']
    
    # process image
    
    mask = (image > threshold).astype('float32')  # set values > th in max to 1
                                                # # set values <= th to 0
    mask_as_list = mask.tolist() # LabVIEW only accepts list as array output
    mask_image_name = 'Mask Image (peak > '+ str(threshold) + ')'
    mask_image_plugin_data = alligator.image_plugin_data(
        Image_Name = mask_image_name,
        Image = mask_as_list
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
    
    return(mask_image_plugin_data)