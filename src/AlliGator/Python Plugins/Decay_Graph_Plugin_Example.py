# Decay_Graph_Plugin_Example.py
# Example AlliGator Decay Graph Python Plugin
# Tested with AlliGator version 0.66
# Author: X. Michalet
# Last modified: 2023-01-04

# The following (triple) comment is needed to tell AlliGator where to
# insert the plugin function(s) as menu item(s)
# the syntax after the AlliGatorTarget = keyword is:
# Window/Type_of_Destination/Destination
# where 'Window' is the target AlliGator window, # 'Type_of_Destination' is
# 'Object' or 'Menu', and 'Destination' is the name of the object,
# or the menu item under which to insert the script's functions as
# 'script_name>>plugin function'
# A single insertion point per window and per object is supported

### AlliGatorTarget = AlliGator/Object/Decay Graph ###
### AlliGatorTarget = AlliGator/Menu/Decay Graph ###

# The following modules are needed to interpret incoming data and send outputs

import json
import alligator

# The double underscores in the function name below will be replaced
# by alternating parentheses in the AlliGator menu (with end spaces trimmed).
# To indicate that the function acts on all selected plots in the graph,
# the function name needs to contain 'Selected_Plots' as part of it.
# To indicate that the function acts on all plots in the graph, the function
# name needs to contain 'All_Plots' as part of it (case non sensitive).
# Otherwise, the function is assumed to act on the right-click selected plot.

def Plot_Scaled_Sum_and_Difference__Selected_Plots__test(
        graph_data_in, params_in_json, addtl_params_out_json_list):
    
    """Scaled Sum & Difference:
    
    Acts on the first two selected plots
    Expects one float parameter (k: float64)
    The resulting k*Sum and k*Difference plots are added to the Decay Graph
    """
    # The following (triple) comment indicates that this function is a plugin
    # This is to distinguish it from accessory functions that should
    # not be imported in AlliGator's menus
    
    ### IsAlliGatorPythonPlugin ###

    # The following (triple commented) section describes which
    # additional parameters are required for that function.
    # If no parameter is needed this section can be ignored
    
    ### AlliGator Input Parameters Definitions ###
    ### k:float64 # scaling parameter
    
    ### Phasor Frequency:AlliGator # This is not visible to the user
    ### Reference Decay:AlliGator # this parameter is treated differently
    ### End of AlliGator Input Parameters Definitions ###
 
    # The following (triple commented) section is mandatory to know which
    # type of output this function returns and which AlliGator
    # object they are destined to

    ### AlliGator Output Value Type & Destination ###
    ### Plots:Decay Graph          # comments are OK
    ### End of AlliGator Output Value Type & Destination ###

    message = 'Scaled Sum of Selected Plots and Phasor Frequency Update'
    exception_type = "None"     # could also be "Warning" or "Error"
    exception_message = ""      # provide verbose information for error

    # decode the parameter string
   
    params = json.loads(params_in_json)
    k = params['k']
    f = params['Phasor Frequency']

    # decode the graph data named tuple
    # the graph data comprises a list of Plot Data
    # Each Plot Data is a named tuple comprised of 
    # a 'Plot_Name' (string)
    # and two lists of double, 'X_Array' and 'Y_Array'

    graph_name = graph_data_in.Graph_Name
    plots = graph_data_in.Plots
    nplots = len(plots)
    
    # Adds and subtracts the first 2 plots if they have the same length
    # otherwise returns an error

    if nplots < 2:
        exception_type = "Error"
        exception_message = "Not enough selected plots!"
        graph_data_out = alligator.graph_plugin_data(
            Graph_Name = graph_name,
            Plots = [],
            Reference_Decay = alligator.empty_plot)
    else:
        plot_data1 = plots[0]
        name1 = plot_data1.Plot_Name
        x1 = plot_data1.X_Array
        y1 = plot_data1.Y_Array
        plot_data2 = plots[1]
        name2 = plot_data2.Plot_Name
        x2 = plot_data2.X_Array
        y2 = plot_data2.Y_Array
        
        # we also requested the Reference Decay, which is an internal data,
        # not a 'parameter'. It is therefore passed as part of the graph_data_in
        # named tuple. If it is not requested, that part of the named tuple will
        # obviously be empty.
        # Other such internal data may be added to graph_data_in in future versions
        # in a (hopefully) backward compatible way.
        # Note that this function DOES NOT use the Reference Decay (aka IRF).
        # This is just to show how to request it and get to the data
        
        ref_decay_data = graph_data_in.Reference_Decay
        ref_decay_name = ref_decay_data.Plot_Name
        ref_decay_x = ref_decay_data.X_Array
        ref_decay_y = ref_decay_data.Y_Array

        # processing of the incoming data
        
        if (len(x1) != len(x2)):
            exception_type = "Error"
            exception_message = "Plots do not have the same length!"
            plots_out = []
        else:
            sumy = []
            for i in range(len(y1)):
                sumy.append(y2[i] + y1[i])    
            diffy = []
            for i in range(len(y1)):
                diffy.append(y2[i] - y1[i])
                
            # we need to repackage those plots into a list of named tuples
            # (same structure as the input)

            plot_data1_out = alligator.plot_plugin_data(
                Plot_Name = 'Scaled Sum of Plots',
                X_Array = x1,
                Y_Array = sumy
            )
            plot_data2_out = alligator.plot_plugin_data(
                Plot_Name = 'Scaled Difference of Plots',
                X_Array = x1,
                Y_Array = diffy
            )
            plots_out = [plot_data1_out, plot_data2_out]
            message = 'Scaled Sum of Selected Plots (scaling factor: ' +\
                str(k) + ', '+name1 + ', '+name2+') and Phasor Frequency Update'
        graph_data_out = alligator.graph_plugin_data(
            Graph_Name = graph_name,
            Plots = plots_out,
            Reference_Decay = alligator.empty_plot)
        
        # Finally, we can send back information on the function outcome
        # and can also set AlliGator Parameters
        # all this packaged in a dictionary, converted to json and
        # appended to the (generally) empty string list
        # addtl_params_out_json_list
        # Note: space and case are irrelevant in the item names
    
    info_out_dict = {
    "Notebook Message" : message,
    "Exception Type" : exception_type,
    "Exception Message" : exception_message,
    "AlliGator:Phasor Frequency" : f # example of internal parameter update
    }
    
    # conversion to JSON string and string is appended to the incoming
    # addtl_params_out_json_list (which is empty in this example)
    # Note that AlliGator will ignore everything but the last string in the list
    
    addtl_params_out_json_list.append(json.dumps(info_out_dict))
    
    # return results to AlliGator

    return(graph_data_out)

    # Note: it is possible to send debug messages to the Python Console
    # using the standard print() statement