.. _phasor-color-map:

Phasor Color Map
================

The Phasor Plot can sometimes be complex to interpret. A additional tool to explore the location in the sample, of pixels characterized by different phasor values, is provided by the Phasor Color Map option of the Source Image's Overlay Mode:



This option uses a color map defined by the user in the Phasor Color Map Picker window opened by right-clicking in the Phasor Plot and selecting the Phasor Color Map Picker menu item:



This opens the Phasor Color Map Picker window:


This window shows an empty phasor plot with the universal circle, in which a polygon can be defined by adding or deleting cursors in the right-hand table (minimum number of vertices: 3, no maximum number). The polygon's interior is colored according to the vertices colors (defined by the cursors' colors) and the Decay Range Exponent parameter. A large exponent will tend to result in sharp boundaries between colored zones, while a small value will tend to blur these boundaries. Negative values of the exponent can also be used for interesting effects.

By checking the Show Color Map Vertices checkbox in the Phasor Plot panel, the same polygon is represented as an overlay (without the color map) in the Phasor Plot:



This allows positioning the polygon's vertices in the Phasor Color Map Picker window where needed in the Phasor Plot.

As the user adjusts the polygon (vertices number, colors and locations), the color map is overlayed on the Source Image:



The Phasor Color Map Picker window can be resized, and the color map saved and reloaded for future use (right-click menu):



The file extension is automatically set to .col.