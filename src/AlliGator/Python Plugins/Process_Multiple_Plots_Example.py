# Process_Multiple_Plots.py
# Example AlliGator Decay Graph Python Plugin
# Tested with AlliGator version 0.67
# Author: X. Michalet
# Last modified: 2023-01-05

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

def Linear_Combination__Selected_Plots__(
        graph_data_in, params_in_json, addtl_params_out_json_list):
    
    """Linear Combination:
    
    Acts on the first two selected plots
    Expects 3 float parameter (a, b, c: float64)
    The resulting a*plot1 + b*plot2 + c is added to the Decay Graph
    """
    # The following (triple) comment indicates that this function is a plugin
    # This is to distinguish it from accessory functions that should
    # not be imported in AlliGator's menus
    
    ### IsAlliGatorPythonPlugin ###

    # The following (triple commented) section describes which
    # additional parameters are required for that function.
    # If no parameter is needed this section can be ignored
    
    ### AlliGator Input Parameters Definitions ###
    ### a:float64 # scaling parameter for plot1
    ### b:float64 # scaling parameter for plot2
    ### c:float64 # vertical offset
    ### End of AlliGator Input Parameters Definitions ###
     
    # The following (triple commented) section is mandatory to know which
    # type of output this function returns and which AlliGator
    # object they are destined to

    ### AlliGator Output Value Type & Destination ###
    ### Plots:Decay Graph
    ### End of AlliGator Output Value Type & Destination ###

    message = 'Linear Combination of Selected Plots'
    exception_type = "None"     # could also be "Warning" or "Error"
    exception_message = ""      # provide verbose information for error

    # decode the parameter string
   
    params = json.loads(params_in_json)
    a = params['a']
    b = params['b']
    c = params['c']
    
    # print(str(a))
    # print(str(b))
    # print(str(c))

    # decode the graph data named tuple
    # the graph data comprises a list of Plot Data
    # Each Plot Data is a named tuple comprised of 
    # a 'Plot_Name' (string)
    # and two lists of double, 'X_Array' and 'Y_Array'

    graph_name = graph_data_in.Graph_Name
    plots = graph_data_in.Plots
    nplots = len(plots)
    
    # combines the first 2 plots if they have the same length
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
        
        # processing of the incoming data
        
        if (len(x1) != len(x2)):
            exception_type = "Error"
            exception_message = "Plots do not have the same length!"
            plots_out = []
        else:
            lincomb = []
            for i in range(len(y1)):
                lincomb.append(a*y1[i] + b*y2[i]+c)    
                
            # we need to repackage those plots into a list of named tuples
            # (same structure as the input)

            plot_data_out = alligator.plot_plugin_data(
                Plot_Name = 'Lin Comb('+name1+','+name2+')',
                X_Array = x1,
                Y_Array = lincomb
            )
            plots_out = [plot_data_out]
            message = 'Linear Combination ['+f'{a:.6G}'+'*plot 1 + '+\
            f'{b:.6G}'+'*plot 2 + '+f'{c:.6G}'+ '] of plot 1: '+name1+\
            ' and plot 2: '+ name2+')'
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
    }
    
    # conversion to JSON string and string is appended to the incoming
    # addtl_params_out_json_list (which is empty in this example)
    # Note that AlliGator will ignore everything but the last string in the list
    
    addtl_params_out_json_list.append(json.dumps(info_out_dict))
    
    # return results to AlliGator

    return(graph_data_out)