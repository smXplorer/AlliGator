.. _phasor-ratio-map:

Phasor Ratio Map
================

The Phasor Ratio discussed in the Phasor Ratio Analysis page of the manual can be used to color-code pixels in the Source Image, creating a Phasor Ratio Map.

This feature involves the Phasor Graph panel (for the definition of both Reference 1 and Reference 2), the Phasor Plot panel (to verify the location of the two references and the range of the map, and obviously, the Source Image.

A typical aspect of the Phasor Plot panel, when the Show References checkbox is checked is shown below:



The two reference phasors are indicated as two dots whose color can be defined in the Phasor Plot page of the Settings window:



In addition to the references, a contour is displayed, which represents the locus of points at a distance 2.5 times the Phasor Ratio Decay Range parameter shown in the figure above. While the contour shows triangular ends, in reality, the domain's boundaries are semi-circular at both ends. The boundary color can be defined in the Settings window as well.

Phasor Ratio Decay Range: The concept of phasor ratio decay range (d0) is use for display purpose only. The color of a pixel characterized by a phasor ratio r is defined by:


where C1 and C2 are the colors of Reference 1 and Reference 2, and d is the distance of the pixel's phasor to the segment connecting Reference 1 and 2. Additionally, any pixel whose phasor's distance from the segment is larger than 2.5  is not attributed any color (i.e. it is not represented on the map). This display option can be turned of by unchecking the Exponential Fading checkbox.

An example of Phasor Ratio Map corresponding to the Phasor Plot figure shown at the top of this page is shown below:



Notice that there are two regions in the specimen characterized by phasors very similar to Reference 1 or Reference 2, and only a few pixels with phasors within the decay range region.
The dark or black pixels correspond to phasors within the decay range region but close to its edge: according to the formula shown above, their color value is close to zero, which corresponds to black. Any pixel with C < exp(-2.5) = 0.082 is not represented in the ovleray.

To hide the Phasor Ratio Map, simply toggle off the Phasor Ratio Map button and refresh the Source Image.

Note: Highlighting ROIs defined in the Phasor Plot in the Source Image doesn't work when the Phasor Ratio Map is shown.