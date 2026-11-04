# Process_Plot.py
# Basic Plot Operations Python Plugin
# Tested with AlliGator version 1.09
# Author: X. Michalet
# Last modified: 2026-10-21

# The following (triple) comment is needed to specify the AlliGator Python 
# Plugin API version number to use

### AlliGator Python Plugin API Version = 1.1.1 ###

### AlliGatorTarget = AlliGator/Object/Decay Graph ###

# Note: this function cannot run from the AlliGator Analysis menu
# because it requires identifying the single selected plot
# by the mouse right-click coordinates

import json
import statistics

import os
os.environ["ALLIGATOR_DEFINITIONS_VERSION"] = "1.1.1"
import alligator_def

def Plot_Mean_and_SDV(
        plugin_data_in, params_in_json, addtl_params_out_json_list):
    
    """Mean & Standard Deviation:
    
    Computes the mean and standard deviation of a plot's values
    """
    
    ### IsAlliGatorPythonPlugin ###

    # since no parameter is needed, no
    # AlliGator Input Parameters Definitions
    # section is needed

    # likewise, since no output object is generated, no
    # AlliGator Output Value Type & Destination
    # section is needed

    message = 'Plot Mean & Standard Deviation'
    exception_type = "None"     # could also be "Warning" or "Error"
    exception_message = ""      # provide verbose information for error

    # decode the graph data named tuple from the plugin data named tuple
    # the graph data comprises a list of Plot Data
    # Each Plot Data is a named tuple comprised of 
    # a 'Plot_Name' (string)
    # and two lists of double, 'X_Array' and 'Y_Array'

    graph_plugin_data = plugin_data_in.Graph_Plugin_Data
    graph_name = graph_plugin_data.Graph_Name
    plots = graph_plugin_data.Plots
    nplots = len(plots)
    
    # Computes the mean and SDV of the Y Array
 
    if nplots == 0:
        exception_type = "Error"
        exception_message = "No selected plot!"
    else:
        plot_data = plots[0]
        name = plot_data.Plot_Name
        x = plot_data.X_Array
        y = plot_data.Y_Array

        # processing of the incoming data
        
        mean = statistics.mean(y);
        SDV = statistics.stdev(y)
           
        message = name + ":\nmean: " + f'{mean:.6G}' + "\nstandard deviation: " +\
            f'{SDV:.6G}'
            
    info_out_dict = {
    "Notebook Message" : message,
    "Exception Type" : exception_type,
    "Exception Message" : exception_message,
    }
    
    # conversion to JSON string and string is appended to the incoming
    # addtl_params_out_json_list (which is empty in this example)
    # Note that AlliGator will ignore everything but the last string in the list
    
    addtl_params_out_json_list.append(json.dumps(info_out_dict))
    
    # since there is no output object returned, the return structure is empty
    
    return()