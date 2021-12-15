# biofilm_channel_width
Script that allows to calculate internal pattern width. It is part of a custom image analysis pipeline, which uses FIJI/ImageJ to extract a line profile signal from a polar-transformed image. 

This script must be used in conjunction with a signal line profile file, which can be obtained in FIJI/ImageJ under "Analyze -> Plot profile". In particular, this script is used for biofilm images with polar geometry, which are pre-processed on FIJI/ImageJ using the Polar Transformer plugin (which can be downloaded at https://imagej.nih.gov/ij/plugins/polar-transformer.html). Briefly, the plugin takes an image which has polar geometry and converts it to an image in Cartesian coordinates (for example, the rim of a circular wheel would be converted to a straight vertical line). The plugin user can assign a number of pixels per degree, which will correspond to the number of pixels in the y direction in the converted cartesian image. 

The pre-processing steps are as follows:
- open microscopy image in FIJI
- launch "Polar transformer" plugin
- enter required information to use the plugin (coordinates of the centre of the object, number of pixels in the y direction for the polar-transformed image)
- draw a vertical line selection across the whole image, at the desired x position (which corresponds to the radial distance from the centre in the original image)
- on the FIJI menu, select "Analyze" and then "Plot profile" to obtain a line profile of the selection
- on the plot, click "Data >> Copy all data" and paste into an Excel spreadsheet
- change column headings in excel to "distance" (first column) and "gray" (second column)
- save the spreadsheet 

The pre-processing steps can be repeated for any number of x positions (= radial positions), which can then be analysed by the script one by one.

An example input file is found in this repository, and is named "test_data". You can use it to run the script. For reference, the dataset was acquired at a radius of 300 um, so you can change the value "radius" to 300 to obtain accurate results for this dataset.

The script outputs an array of widths, calculated across the line profile which is read in at the beginning of the script. These widths can be saved into a new spreadsheet for further analysis. 
