#title           : get_lld_setting_dialog.py
#description     : Sub-module of Get LLD Tool, a QGIS Python Plugin.
#		 : Loads the Qt UI and intializes the widget
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

# Generic system import
import os

# Library import - PyQt
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'get_lld_settings_dialog.ui'))


class settingsDialog(QtWidgets.QDialog, FORM_CLASS):
	"""  Load the Qt UI and initialize """
	def __init__(self, parent=None):
		super(settingsDialog, self).__init__(parent)
		self.setupUi(self)
