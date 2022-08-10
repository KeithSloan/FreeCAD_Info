#***************************************************************************
#*   (c) Keith Sloan (keith@sloan-home.co.uk) 2012                         *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU General Public License (GPL)            *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with FreeCAD; if not, write to the Free Software        *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#*   Keith Sloan 2012                                                      *
#***************************************************************************
import FreeCAD
import FreeCADGui
import Part

import PySide2
from PySide2 import QtGui , QtCore, QtWidgets

def translate(context, text):
    return QtWidgets.QApplication.translate(context, text, None)

def utf8(unio):
    return unicode(unio).encode('UTF8')

class Information():
    def IsActive(self):
        return bool(FreeCADGui.Selection.getSelectionEx())
        #return bool(FreeCAD.ActiveDocument.Objects)

    def Activated(self):
        panel = AddInfoTask()
        selection=FreeCADGui.Selection.getSelectionEx()
        v = 0
        a = 0
        if len(selection) > 0:
                objs=[selobj.Object for selobj in selection]
        for i in objs:
            v = v + i.Shape.Volume
            a = a + i.Shape.Area
        if len(selection) == 1:
            s = objs[0].Shape
            print(s.ShapeType)
            print(s.Solids)
            c = s.Solids[0].CenterOfMass
            panel.form.Xvalue.setText(str(c.x))
            panel.form.Yvalue.setText(str(c.y))
            panel.form.Zvalue.setText(str(c.z))
            m = s.Solids[0].MatrixOfInertia
            print(m)
            panel.form.Xaxisvalue.setText(str(m.A11))
            panel.form.Yaxisvalue.setText(str(m.A22))
            panel.form.Zaxisvalue.setText(str(m.A33))

            #c = Part.cast_to_shape(objs[0].Shape).CenterOfMass

            #else:
                #    objs=FreeCAD.ActiveDocument.Objects
        #    for i in objs:
        #        print i.Shape.Volume
        #    i = len(objs) - 1
        #    v = objs[i].Shape.Volume
        #    a = objs[i].Shape.Area
        #    #print(objs)

        panel.form.volvalue.setText(str(v))
        panel.form.areavalue.setText(str(a))
        FreeCADGui.Control.showDialog(panel)
    
    def GetResources(self):
        return {'Pixmap': 'python', 'MenuText': 'Shape Inform', 'ToolTip': 'Shape Information'}



class AddInfoWidget(QtWidgets.QWidget):
    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.textEdit = QtWidgets.QTextEdit()
        self.vollabel = QtWidgets.QLabel('Volume')
        self.volvalue = QtWidgets.QLineEdit()
        self.areaLabel = QtWidgets.QLabel('Surface Area')
        self.areavalue = QtWidgets.QLineEdit()
        self.comlabel = QtWidgets.QLabel('Centre of Mass')
        self.Xlabel = QtWidgets.QLabel('X')
        self.Xvalue = QtWidgets.QLineEdit()
        self.Ylabel = QtWidgets.QLabel('Y')
        self.Yvalue = QtWidgets.QLineEdit()
        self.Zlabel = QtWidgets.QLabel('Z')
        self.Zvalue = QtWidgets.QLineEdit()
        self.moilabel = QtWidgets.QLabel('Moment of Interia about C.O.M')
        self.Xaxislabel = QtWidgets.QLabel('X Axis')
        self.Xaxisvalue = QtWidgets.QLineEdit()
        self.Yaxislabel = QtWidgets.QLabel('Y Axis')
        self.Yaxisvalue = QtWidgets.QLineEdit()
        self.Zaxislabel = QtWidgets.QLabel('Z Axis')
        self.Zaxisvalue = QtWidgets.QLineEdit()

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.vollabel, 0, 0)
        layout.addWidget(self.volvalue, 0, 1)
        layout.addWidget(self.areaLabel, 1, 0)
        layout.addWidget(self.areavalue, 1, 1)
        layout.addWidget(self.comlabel, 2, 1)
        layout.addWidget(self.Xlabel, 3, 0)
        layout.addWidget(self.Xvalue, 3, 1)
        layout.addWidget(self.Ylabel, 4, 0)
        layout.addWidget(self.Yvalue, 4, 1)
        layout.addWidget(self.Zlabel, 5, 0)
        layout.addWidget(self.Zvalue, 5, 1)
        layout.addWidget(self.moilabel, 6, 1)
        layout.addWidget(self.Xaxislabel, 7, 0)
        layout.addWidget(self.Xaxisvalue, 7, 1)
        layout.addWidget(self.Yaxislabel, 8, 0)
        layout.addWidget(self.Yaxisvalue, 8, 1)
        layout.addWidget(self.Zaxislabel, 9, 0)
        layout.addWidget(self.Zaxisvalue, 9, 1)

        self.setLayout(layout)
        self.setWindowTitle(translate('Info', u'Object Information'))

class AddInfoTask():
    def __init__(self):
        self.form = AddInfoWidget()
        #self.form.buttonadd.clicked.connect(self.addelement)

    def getStandardButtons(self):
        return int(QtWidgets.QDialogButtonBox.Close)

    def isAllowedAlterSelection(self):
        return True

    def isAllowedAlterView(self):
        return True

    def isAllowedAlterDocument(self):
        return True



FreeCADGui.addCommand('Information', Information())
