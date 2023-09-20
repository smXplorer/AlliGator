.. _alligator-decay-fitting:

.. From AlliGator:Fluorescence Decay Fitting

Fluorescence Decay Fitting
==========================

AlliGator offers basic capabilities to analyze data using standard techniques of fluorescence decay fitting:

- Individual decays can be fitted with a single or double-exponential decay model convolved with an experimental instrument response function (IRF).
- Multiple ROIs in the image source can be fitted instead of their phasor calculated, the resulting parameters being output as maps (see :ref:`alligator-decay-fit-parameter-map-panel`)
- Time series analysis of a ROI in the image source can use "Series Fit" instead of "Series Phasor" (each time point decay is fitted with the same model, and selected parameters are output as time-series).
- Selected decays can be globally fit to a single or double-exponential decay convolved with an experimental IRF, some parameters of the model being common to all decays.

These different capabilities are described next.

Single decay fit
----------------

Overview
++++++++

A single plot can be fitted by a model function convolved with the selected IRF by right-clicking on its legend (or close to it in the graph) and selecting Fit Decay. The parameters specifying the type of fit and constraints used are defined in the Settings >> Fluorescence Decay >> Fit Options panel reproduced below:

<insert figure here>

Several fit options, discussed below, are available:

- Model
- Method
- Algorithm 
- Weighted Fit
- Show Fit Residuals
- Type of Residuals
- Max & Min Decay Percentile
- Show Full Decay
- Parameter Uncertainties
- Periodic Boundaries
- Termination Criteria
- Use Local IRF

Parameter constraints, guess parameters and whether or not to display the output as plots are managed in the  Settings >> Fluorescence Decay >> Fit Parameters panel

- Fit with constraints applied on individual parameters is handled by an array of Fit Parameter Constraints specifying the:
    + Parameter
    + Min & Max Value
    + whether or not it is a Global parameter (applicable in case of multiple fits only)
    + whether the constraint is used or not
- Guess parameters can be provided in the corresponding array by selecting the parameter name and providing the guess value. Additionally, two options can be turned on or off:
    + Use Guess Parameters
    + Use Last Fitted Parameters
- The Displayed Fit Parameters array only applies to time-series analysis and will be discussed in that context in a later section.

Fit Options
+++++++++++

- Fit Model: Two models are currently available.

A single exponential (1-Exponential) model defined by:

:math:`f\left( t \right) = {A_1}\exp \left( { - \frac{t}{{{\tau _1}}}} \right) + b`

where b is the baseline and the IRF is offset by an amount (i.e. centered at) :math:`t_0`.

A double exponential (2-Exponentials) model defined by:

:math:`f\left( t \right) = {A_1}\exp \left( { - \frac{t}{{{\tau _1}}}} \right) + {A_2}\exp \left( { - \frac{t}{{{\tau _2}}}} \right) + b`,

- Fit Weight: Two types of fits can be performed:

an unweighted fit where all data points are equally weighted in the minimization function (sum of difference squared), or a weighted fit, where each data point i is weighted by :math:`1/{f_i}`  (or 1 if :math:`f_i = 0`), where :math:`f_i` is the function value.

- Residuals: The fit residuals (difference between the original decay and its fit) can be optionally plotted in addition to the fit itself. Several weighting schemes can be chosen:

<insert figure here>

The standard residual is the mere difference between the original decay and its fit, while the normalized residual is the difference divided by the function value. The reduced residual is the difference divided by the square root of the absolute value of the function value.

- Min & Max Decay Percentile: The fit can be performed over the whole decay or limited to the "tail" part of the decay. The latter is defined as the part of the decay located between XX% of the decay maximum (max percentile) and YY% (:math:`0  \le  YY  <  XX  \le  1`) of the decay maximum (min percentile).

- Show Full Decay: When only part of the decay is fitted, it is possible to show the fitted curve (and residuals, optionally) calculated over the full decay range by checking this checkbox. The default (unchecked) is to only show the decay over the selected range.

- Parameter Uncertainties: Because parameter uncertainty calculation involves computing the covariance matrix of all parameters, this can be very memory consuming in the case of global fit of large data sets. In that case, it might be desirable to skip calculation of parameter uncertainties by leaving this checkbox unchecked.

- Periodic Boundaries: This option is available in beta mode and allows enforcing periodic boundary conditions (and provide a value for the repetition period).

<insert figure here>

This is mostly useful for large gates (e.g. SwissSPAD data) for which the resulting decay does not look anymore as a sharp rise followed by a tail decaying to background level, but instead as a continuous "wave". In these conditions, it is advantageous to treat the decay as periodic. Note that the recorded decay needs to be no longer than the provided period for the fit to be any good (it can be shorter, i.e. truncated). This option has no effect on global fits at this time.

Fit Parameter Constraints
+++++++++++++++++++++++++

Fit parameters can be constrained within a specified range defined by the min (-Inf if unconstrained) and max value (Inf if unconstrained).

The list of actual parameters that can be constrained depends on the chosen model:

For instance, choosing :math:`tau_2` as a constrained parameter in a 1-Exponential model will have no effect.

If a parameter is unconstrained, it is possible to remove it from the array of constrained parameters by right-clicking on it and choosing Delete Element. If no parameter is constrained, it is possible to delete all elements of the array by right-clicking on the scrollbar and choosing Empty Array.

Fit Results
+++++++++++

In addition to the plot output(s) in case of a successful fit, the fit results are output to the Notebook. A typical output will read
::

    2-Exponentials unweighted fit of XXXXX
    Fit range: 0%-100%
    Fitted Parameters:
    Offset: 0.003166 ± 0.001487 [-0.1, 0.1]
    Baseline: -0.003543 ± 0.004714
    A1: 0.26873 ± 0.140506 [0, Inf]
    tau 1: 0.446588 ± 0.151041 [0.005, 1]
    A2: 1.122693 ± 0.144699 [0, Inf]
    tau 2: 1.13671 ± 0.078737 [0, 2]
    R^2: 0.999408
    Reduced Chi^2: 0.007177
    Standard residuals

where XXXXX is the decay name. {R^2} and the reduced {:math:`\chi ^2`} as well as the 68% confidence intervals (errors) are defined according to the definitions provided here.
If the fit fails, an error message will be displayed instead (and not plot added to the Decay Graph).

Time-series decay fit
---------------------

In the case of a time-series analysis, decay fits can be performed instead of phasor analysis, by choosing Time-Series Analysis (Fitting) in the Analysis menu:

<insert figure here>

Each time point decay is fitted separately, following the protocol described previously for single decays. In addition, it is possible to generate one or more plots of the evolution of selected fit parameters across the series, using the Displayed Fit Parameters array. These plots will be output in the Lifetime Graph of the Lifetime Analysis panel (see corresponding manual page). Parameters that can be displayed can be chosen from the following list:

<insert figure here>

This list includes the fit parameters and derived quantities, such as the mean lifetime <tau> or fraction f1 and f2 (for the 2-Exponentials model, defined below), or the :math:`R^2` and :math:`\chi ^2` outputs.

:math:`\left\langle \tau  \right\rangle  = \frac{A_1\tau _1 + A_2\tau _2}{A_1 + A_2}`

:math:`f_1 = \frac{{{A_1}{\tau _1}}}{{{A_1}{\tau _1} + {A_2}{\tau _2}}}`

:math:`f_2 = 1 - f_1`