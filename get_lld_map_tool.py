#title           : map_tool.py
#description     : Sub-module of Get LLD Tool, a QGIS Python Plugin.
#		 : Captures and returns map coordinates back to main function
#author          : Casey McMahon
#date            : 2020-01-06 (YYYY-MM-DD)
#version         : 1.0
#usage           : QGIS 3.4+ (GUI Plugin)
#notes           : Considered Complete
#python_version  : 3.7.5
#copyright	 : (C) 2020 By Casey McMahon
#license notice  : This file is part of 'Get LLD Plugin'
#		 
#		   Get LLD Plugin is free software: you can redistribute it or modify  
#		   it under the terms of the GNU General Public License as published by
#		   the Free Software Foundation, either version 3 of the License, or
#		   (at your option) any later version.
#
#		   This program is distributed in the hope that it will be useful,
#		   but WITHOUT ANY WARRANTY; without even the implied warranty of
#		   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#		   GNU General Public License for more details.
#
#		   You should have received a copy of the GNU General Public License
#		   along with Get LLD Plugin. If not, see <https://www.gnu.org/licenses/>.
#===========================================================================================

# Library imports - PyQt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCursor, QPixmap
from PyQt5.QtWidgets import QApplication

# Library imports - QGIS
from qgis.gui import QgsMapToolEmitPoint, QgsVertexMarker
from qgis.core import (QgsCoordinateReferenceSystem,
		       QgsCoordinateTransform,
                       QgsProject)

class pointTool(QgsMapToolEmitPoint):
	""" Point map tool to capture cursor click coordinates """ 

	def __init__(self, canvas):
		QgsMapToolEmitPoint.__init__(self, canvas)
		self.canvas = canvas
	
	canvasClicked = pyqtSignal('QgsPointXY')
	def canvasReleaseEvent(self, event):
		""" register a click from user and emit a XY point in WGS84 coords """
		
		# Get canvas coordinate reference system code
		crs_canvas = self.canvas.mapSettings().destinationCrs()
		
		# Create variable for point pending tranformation
		point_canvas_crs = event.mapPoint()
		
		# Place WGS84 CRS into variable then create transformer variable
		wgs = QgsCoordinateReferenceSystem(4326)
		transformer = QgsCoordinateTransform(crs_canvas, wgs, QgsProject.instance())
		
		# transform the CRS and emit a signal with QgsPointXY variable
		point_wgs = transformer.transform(point_canvas_crs)
		self.canvasClicked.emit(point_wgs)
