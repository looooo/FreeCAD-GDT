#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2016 Juan Vanyo Cerda <juavacer@inf.upv.es>             *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

from .gdt import *
import  DraftTools
from .gdt import ICON_DIR

gdt = GDTWidget()
gdt.dialogWidgets.append( fieldLabelWidget(Text='Offset:') )
class AnnotationPlaneCommand:
    def __init__(self):
        self.iconPath = str(ICON_DIR / 'annotationPlane.svg')
        self.toolTip = 'Add Annotation Plane'
        self.dictionary = []
        for i in range(1,100):
            self.dictionary.append('AP'+str(i))
        self.idGDT = 4

    def Activated(self):
        showGrid()
        gdt.activate(idGDT = self.idGDT, dialogTitle=self.toolTip, dialogIconPath=self.iconPath, endFunction=self.Activated, dictionary=self.dictionary)

    def GetResources(self):
        return {
            'Pixmap' : self.iconPath,
            'MenuText': self.toolTip,
            'ToolTip':  self.toolTip
            }

    def IsActive(self):
        if len(getSelection()) == 1:
            return (getSelectionEx()[0].SubObjects[0].ShapeType == 'Face')
        else:
            return False

FreeCADGui.addCommand('dd_annotationPlane', AnnotationPlaneCommand())
