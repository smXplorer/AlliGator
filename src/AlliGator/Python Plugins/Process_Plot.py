# Process_Plot.py
# Basic Plot Operations Python Plugin
# Tested with AlliGator version 0.66
# Author: X. Michalet
# Last modified: 2023-01-04

### AlliGatorTarget = AlliGator/Object/Decay Graph ###
### AlliGatorTarget = AlliGator/Menu/Decay Graph ###

import json
import alligator
import statistics

def _Plot_Mean_SDV(
        graph_data_in, params_in_json, addtl_params_out_json_list):
    
    """Mean & Standard Deviation:
    
    Computes the mean and standard deviation of a plot's values
    """
    
    ### IsAlliGatorPythonPlugin ###

    message = 'Plot Mean & Standard Deviation'
    exception_type = "None"     # could also be "Warning" or "Error"
    exception_message = ""      # provide verbose information for error

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
    
    return()