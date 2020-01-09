#title           : __init__.py
#description     : Sub-module of Get LLD Tool, a QGIS Python Plugin.
#		 : Initializes the plugin on startup
#author          : Casey McMahon
#date            : 2020-01-09 (YYYY-MM-DD)
#version         : 0.1
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

from .get_lld import get_lld_plugin

def classFactory(iface):
    return get_lld_plugin(iface)
