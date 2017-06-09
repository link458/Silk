#    This file is part of Silk
#    (c) Edward Mills 2016-2017
#    edwardvmills@gmail.com
#	
#    Silk is the user interface of ArachNURBS. This implementation is a FreeCAD workbench.
#
#    Silk is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


from __future__ import division # allows floating point division from integers
import FreeCAD, Part, math
from FreeCAD import Base
from FreeCAD import Gui
import ArachNURBS as AN

class ControlPoly4():
	def Activated(self):

		sel=Gui.Selection.getSelection()
		if len(sel)==1:
			if sel[0].GeometryCount==3:
				mode='3L'
			else: #if sel[0].GeometryCount==1 or sel[0].GeometryCount==8:
				mode='FirstElement'
		elif len(sel)==2:
			mode='2N'
		print mode
		if mode=='3L':
			sketch=Gui.Selection.getSelection()[0]
			a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","ControlPoly4_3L")
			AN.ControlPoly4_3L(a,sketch)
			a.ViewObject.Proxy=0 # just set it to something different from None (this assignment is needed to run an internal notification)
			a.ViewObject.LineWidth = 1.00
			a.ViewObject.LineColor = (0.00,1.00,1.00)
			a.ViewObject.PointSize = 4.00
			a.ViewObject.PointColor = (0.00,0.00,1.00)
			FreeCAD.ActiveDocument.recompute()

		if mode=='FirstElement':
			sketch=Gui.Selection.getSelection()[0]
			a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","ControlPoly4_FirstElement")
			AN.ControlPoly4_FirstElement(a,sketch)
			a.ViewObject.Proxy=0 # just set it to something different from None (this assignment is needed to run an internal notification)
			a.ViewObject.LineWidth = 1.00
			a.ViewObject.LineColor = (0.00,1.00,1.00)
			a.ViewObject.PointSize = 4.00
			a.ViewObject.PointColor = (0.00,0.00,1.00)
			FreeCAD.ActiveDocument.recompute()

		if mode=='2N':
			sketch0=Gui.Selection.getSelection()[0]
			sketch1=Gui.Selection.getSelection()[1]
			a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","ControlPoly4_2N")
			AN.ControlPoly4_2N(a,sketch0,sketch1)
			a.ViewObject.Proxy=0 # just set it to something different from None (this assignment is needed to run an internal notification)
			a.ViewObject.LineWidth = 1.00
			a.ViewObject.LineColor = (0.00,1.00,1.00)
			a.ViewObject.PointSize = 4.00
			a.ViewObject.PointColor = (0.00,0.00,1.00)
			FreeCAD.ActiveDocument.recompute()
	
	def GetResources(self):
		return {'Pixmap' :  FreeCAD.__path__[3] + '\Silk\Resources\Icons\ControlPoly4.svg', 'MenuText': 'ControlPoly4', 'ToolTip': 'ControlPoly4: \n Creates a 4 point control polygon from a variety of inputs'}

Gui.addCommand('ControlPoly4', ControlPoly4())
