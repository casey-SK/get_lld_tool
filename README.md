# Get LLD Tool - QGIS Plugin

![](https://github.com/casey-SK/get_lld_tool/blob/master/logo.png)

## What is it?

Get LLD Tool is a QGIS plugin to get the Legal Land Description (Township Reference System) of a point using a toggle button. A useful tool for when a coworker asks you for a LLD while you are working in QGIS. The Township Reference System is used across the three prairie provinces of Canada ( also known as ATS, SaskGrid, & DLS). It also sees some use in the USA northern states.

The tool toggles on and off like the editing button. While turned on, a new cursor appears on the map canvas. If you click on the canvas, a message bar will appear telling you the LLD of the location you just clicked on. 

## NOTE

The TRS grid is not unified, each province manages it's own grid and at least one of the provincial governments makes the grid proprietary property that you must pay for. For this reason, the program requires the user to setup the tool to point to a stored LLD grid layer that they own themselves and can access from their computer. At least it can be stored in any format (shapefile, geopackage, PostGIS layer, etc.). The plugin is flexible in how it may parse the data to display the message. Follow the quickstart guide for details.

## QUICKSTART
Work in Progress

## Example
![](https://github.com/casey-SK/get_lld_tool/blob/master/img/get_lld_program_example_2020-01-09.png)

## TODO
- [] Modify Settings UI to enable user input
- [] Enable plugin to store user defined defaults (location of lld layer)
- [] Return function for OK and Apply buttons
- [] Create print message (with GoTo button) when a user tries to click on the canvas without defining an LLD layer
- [] Add buffer around points to prevent road allowances from confusing users
- [] Create print message when invalid location is picked (something like 'outside of provided grid extent')
