.. _alligator-decay-preprocessing:


.. From AlliGator:Fluorescence Decay

Decay Pre-processing
====================

A number of options and operations can be applied to ROI decays. Those are defined in the **Settings:Fluorescence Decay:Basic Analysis** window.

Warning: Some options only take effect after the file is reloaded. Those are indicated with an asterisk in parenthesis (*) after their label in the Settings window, and in the text below.

Up until version 0.18.1, the order of operations was:

- Pile-up Correction
- Background Correction
- Revert
- Normalize
- Smoothen
- Shift
- Extrapolate
- Straighten

In version 0.18.2, the order of operations was changed to:

- Pile-up Correction
- Background Correction
- Revert
- Smoothen
- Straighten
- Shift/Rotate
- Extrapolate
- Normalize

Moreover, the way the "Shift" operation functions was modified in 0.18.2, to include an option to apply a constant shift (the "Default" mode) and an option to make this shift "Rotate" the decay, by assuming that the dataset is periodic.

In later versions (0.19 and following), the order of the decay pre-processing operations (except for pile-up correction, which is always performed first) became user-selectable. In the case of photobleaching or photobrightening, this allows correcting for that effect before attempting a square-gated single-exponential background subtraction, for instance.
To change the order of operations, right-click on the Operations Order list and select Reorder operations:
This will open a window showing the current list order:
Selecting any of the items, use the buttons at the bottom to change the location of that item in the list. When done, click the OK button (rightmost button) to accept and close the window, or the Cancel button (leftmost button) to cancel any modifications to the original list. Closing the window is equivalent to cancelling and accepting that choice.

1. Gate Selection

1.1 Gate Duration: The gate duration parameter is currently only used to calculate the Universal Curve (aka pseudo universal circle).

1.2. Gate Separation: The gate separation specifies the temporal offset between gates.

1.3. Gate Step (*): The default calculation mode is to use all gates to build the decay plot. However, it is possible to use only one every n gates, by specifying n in the value of Gate Step. The effect of choosing to use n = 8 (rather than the default n = 1) is shown on the figure below.
1.4. Gates to Skip (*): Two other parameters defined in the Settings>>Fluorescence Decay>>Basic Analysis panel affect the final shape of the decay:

    Decay Points to Skip: Start
    Decay Points to Skip: End

These parameters define how many gate images are omitted when loading the datasets. Specifically, if Start = s,  End = e, and each dataset is comprised of N gates, only gates s+1, s+2, ..., n - e-1, n - e will be retained in the analysis. This can be useful if decay inspection reveals some unphysical "feature" at the beginning or end of the decays.

Warning: Changing these two parameters after the dataset has been loaded has no effect on subsequent analysis. For these parameters to take effect, the dataset needs to be reloaded.

2. Pile-up Correction (*)

When selected, this option gives access to the pixel well capacity (Max Value), which, in SwissSPAD data, corresponds to the number of 1-bit frames accumulated for each gate image. The correction applied takes into account the possibility of pile-up (missed counts) at high count rates, according to:

S = - N log(1 - R/N)

where R is the raw count, N is the pixel well capacity parameter and S the corrected count value.
3. Background Subtraction

The Background Subtraction checkbox is used to perform automatic background subtraction from all computed decays (as well as when computing the Phasor Plot Image) in one of the following manners.


3.1. Baseline subtraction based on a reference window

As can be noticed in the plot shown above, it is customary in time-gated imaging experiments to offset the decay on the time axis in such a way that a flat (background) zone precedes the actual rise and decay. This can therefore be used to estimate the background for each ROI (and by extension, for each pixel). In AlliGator, the user needs to define the Min Gate and Max Gate values to be used for background estimation. This is done in the Settings>>Fluorescence Decay panel (see Figure below). The  actual value retained as background is the minimum (Min) or average (Mean) value recorded in this gate interval, depending on the chosen Method. 


3.2. Square Gated Single-Exponential method

In this approach (Square Gated Single-Exponential), the recorded decay is assumed to be the result of a single-exponential decay integrated over a square gate of duration W (See description in ref. 2 in the Bibliography page). The user needs to provide the gate positions where the known minimum (Min Gate) and maximum (Max Gate) of the decay are observed (best obtained by looking them up on a reference decay with high SNR). The analysis computes the baseline value (Background), Amplitude and Lifetime associated with the decay and displays them on the top right of the Fluorescence Decay panel. These parameters as well as the total integrated intensity are associated with the decay and the corresponding phasor plot data point (Phasor Graph panel).

3.3. Background file method

Another method consist in choosing a time-gated data file (preferably acquired using the same settings as the data to be analyzed) corresponding to pure background signal. Selection of the File method will show a Background File selection box, with which this file can be selected. Subsequently, this file's data will be subtracted from new datasets, pixel-by-pixel and gate-by-gate, prior to processing.
The Background Scaling Factor parameter (default value: 1) can be used to adjust the amount of background file correction. Using a value larger F, each gate image i will be subtracted the corresponded background gate image i times F. This allows adjusting for different acquisition parameters between data and background acquisition.

Important Note: When the background file subtraction method is selected, any change to the background file (or switching from a different method to the background file subtraction method) requires the current datafile to be reloaded. Indeed file background subtraction happens when the dataset is loaded.

Warning: Note that when the background file subtraction method is selected, the position of the Background subtraction method in the Operation Order list is ignored (it is always performed first).

4. Reverse Gates (*)

When selected it, changes the direction of the plotted decay, so that the tail of the decay comes after the rising part. This option is needed for some SwissSPAD datasets.

5. Normalization

Checking the Normalize Decay checkbox will apply a simple normalization (division by the maximum decay value) to each decay before display.

6. Decay Smoothing

Occasionally, a decay may be affected by undesirable "spikes". It is sometimes possible to remove those spikes using cubic basic spline smoothing (details can be found at http://zone.ni.com/reference/en-XX/help/371361P-01/gmath/cubic_spline_fit/). The Cubic Spline Fit implementation of LabVIEW is used without weights, and smoothness parameters identically equal to 1 for all points, and balance parameter equal to 1 -10^(-x), where x is the Smoothing Parameter defined in the Settings>>Fluorescence Decay>>Basic Analysis panel. From the Cubic Spline Fit description page linked to above:

    If x = 0, the cubic spline fit is equivalent to a linear fit. If x = Inf, the cubic spline fit interpolates between the data points.
    If x < 0, an appropriate value is automatically calculated according to the time axis values.

To use this algorithm as part of the decay pre-processing, check the Smoothen Decay checkbox. The only exposed parameter for this algorithm, Smoothing Parameter, is accessible in the Settings>>Fluorescence Decay panel.
Alternatively, an existing decay can be post-processed (creating a new curve) using the Smooth Plot function of the Context Menu (see below).

7. Decay Shift

Decays can occasionally "shift" along the time axis due to several possible causes (in general, setup instabilities). While this is normally not causing problems if data is properly calibrated, it is possible to force alignment of all decays along the time axis by checking the Shift Decay checkbox. There are several options associated with this functionality.

    Type: this drop-down list gives access to 4 modes described below:

    Rotate: this checkbox specifies whether the shift results in a rotation of the decay (considered periodic) or whether to pad the decay with zeros and discard points corresponding to negative abscissa.
    Shift: this parameter has different interpretation depending on the type of shift selected (see below for details) and is not always visible.
    Threshold: this parameter is used in the Threshold mode only (see below for details).

Decay shift modes details

    Default: in this case, a constant shift is applied to all decays. This can for instance be useful to align the peak of a given sample to the zero point, or align decays acquired with different setups, etc.
    CFD: the constant fraction discrimination mode applies a constant shift to each decay before inverting it (multiplying it by -1) and adding it to the original decay. The effect of this operation, provided the shift is of the order of the IRF width or smaller, is to create a curve looking like a "chirp", with a positive bump followed by a negative one, with a zero point in between. This point is generally stable if the shape of the decay is relatively constant (the amplitude can vary). The position of the zero-crossing point is then compared to that of a Reference Decay (see section 9 below for details on how to define a Reference Decay) and the difference between these two positions is defined as the decay shift.
    Threshold: in this mode, the provided Threshold parameter (the Shift parameter is not available) is used to find the first location in the decay where this threshold is crossed (from below). This location is compared to that obtained for the Reference Decay (see section 9 below for details on how to define a Reference Decay) and the difference between these two positions is defined as the decay shift.
    Cross-Correlation: in this mode, the CC of the decay and the Reference Decay (see section 9 below for details on how to define a Reference Decay) is computed and the position of its maximum determined and returned as the decay shift.

At the end of a series of decay analysis, it is possible to plot the calculated shifts in the Lifetime Graph of the Lifetime Analysis panel, using the Plot Decay Shifts context menu item in that graph.

8. Decay Straightening

Occasionally, samples can photobleach (or photobrighten) during the course of a series of gate acquisition. This phenomenon is identifiable by the fact that the recorded gate value at the end of a complete laser period is different (generally smaller but sometimes larger) than at the beginning of the period. The straighten function assumes that this is due to an exponential decay (or increase) of the signal due to some underlying uncontrollable phenomenon, and attempts to calculate the time scale of this variation as well as its amplitude, and finally, correct for it accordingly throughout the gate series.
Up until version 0.18.1, this correction was applied as follows:


where {F_{\min }} is the minimum decay value, T is the period, \tau  is the photobleaching/photobrightening time constant obtained from:


The sign of \tau  obtained from the above equation handles both cases.
After version 0.18.2, the correction does not consider that the decay consists of a constant background ({F_{\min }}) added to a photbleaching/photobrightening component, as this background component should be taken care of by the background subtraction step, which usually precedes (*) all other pre-processing steps (except pile-up correction). As a consequence, the formula becomes:

where \tau  is given by:
This equation requires that F(0) and F(T) be non-zero.
(*) Note that since version 0.19, it is possible to change the order of the different decay pre-processing operations (except pile-up correction, which remains the first operation). This means that if background correction follows decay straightening, the assumption of the straightening algorithm may be incorrect (i.e. the algorithm will assume that both decay and background exponentially increase or decrease with the same time constant).

9. Decay Extrapolation

In case the decay tail doesn't reach the background level, the resulting phasor will be offset by an amount that will depend on the final value reached by the decay. It is possible to compensate artificially for this truncation by extrapolating the decay with an exponential tail. The parameters defining the range of this extrapolation are defined in Settings>>Fluorescence Decay>>Basic Analysis:
The Tail Fraction parameter specifies what fraction of the decay (starting from the end) is used to perform a fit to a single exponential decay. The Additional Points parameter specifies by how many points (spaced as in the original decay) to add to the decay.
The Extrapolate Decay checkbox only applies when computing decays from scratch. If checked, the computed decays are automatically extrapolated.

10. Other Decay Processing Functions

Other decay processing functions are accessible via the Decay Graph context menu. Most of the context menu items are self-explanatory. Items are grouped in different categories of functions:

    Edit plot
    Visibility (and plot style) functions
    Deletion functions
    Save functions
    Load Plot(s)
    Plot processing
    Fitting functions
    IRF-related functions
    Graph copy/export/visibility functions

As for all graphs in AlliGator, the checkboxes in front of plot names in the graph legend have a dual function. When checked, the plot is visible AND selected. When unchecked, the plot is hidden AND deselected.

Single plot functions can be used by right-clicking on the plot of interest in the graph or its legend. Note that the Export menu is a bit different in this respect: to export a single plot to the clipboard as an ASCII formatted data set, right-click on that plot's legend (the graphic part of it). To export the WHOLE graph (including hidden plots), right-click in the graph region.
Selected plots (or individual plots) can be directly saved in an ASCII file using the Save functions of the above menu.

10.1. Edit Plot

This menu item opens the plot on which the user has right-clicked in the Plot Editor, where several basic operations can be performed.

Warning: the edited plot replaces the original plot unless the Copy button is pressed. It is possible to cancel the operation at any time while in the Plot Editor.

Plot Editor functionalities are described in the corresponding page of the manual.

10.2. Process Plot submenu

    y >> f(y) Transform: selecting this item opens up a dialog window to enter an algebraic formula:

The corresponding amplitude values of the plot (y) will be modified and replaced by y' as defined by the formula (assuming that the syntax is correct. For a list of supported functions, please refer to this LabVIEW help page).

    (x, y) >> (f, g)(x, y) Transform: selecting this item  opens up a dialog window to enter an algebraic formula:

The corresponding time (x) and amplitude (y) values of the plot will be modified and replaced by (x', y') as defined by the formulas (assuming that the syntax is correct. For a list of supported functions, please refer to this LabVIEW help page).

    Smoothen Plot: see the  Decay Smoothing section above for a description of this operation. The difference is that this menu item allow performing this operation after the decay as been computed and displayed, rather than at the time it is extracted from the dataset.
    Denoise Plot: When smoothing by cubic spline provides unsatisfactory results, the Denoise Plot function may provide better results. This function relies on wavelet analysis routines of the LabVIEW Advanced Signal Processing Toolkit, detailed at http://zone.ni.com/reference/en-XX/help/371419D-01/lvwavelettk/wa_de_noise/. Parameters can be set in the Settings>>Fluorescence Decay>>Advanced Analysis tab:

    Average Selected Plots: This function does what it says and creates an additional plot.
    Compute Cumulative Function: This function can be useful to define what fraction of a decay to fit, as discussed in doi: 10.1117/1.3469797.
    Straighten Decay: see the  Decay Straightening section above for a description of this operation. The difference is that this menu item allow performing this operation after the decay as been computed and displayed, rather than at the time it is extracted from the dataset.
    Extrpolate Decay: see the  Decay Extrapolation section above for a description of this operation. The difference is that this menu item allow performing this operation after the decay as been computed and displayed, rather than at the time it is extracted from the dataset.