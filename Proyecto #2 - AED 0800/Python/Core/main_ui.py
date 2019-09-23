# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(529, 541)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.btnCargarArchivo = QtWidgets.QPushButton(Form)
        self.btnCargarArchivo.setObjectName("btnCargarArchivo")
        self.gridLayout.addWidget(self.btnCargarArchivo, 3, 0, 1, 1)
        self.btnCrearMapa = QtWidgets.QPushButton(Form)
        self.btnCrearMapa.setObjectName("btnCrearMapa")
        self.gridLayout.addWidget(self.btnCrearMapa, 3, 1, 1, 1)
        self.txtText1 = QtWidgets.QTextEdit(Form)
        self.txtText1.setObjectName("txtText1")
        self.gridLayout.addWidget(self.txtText1, 0, 0, 1, 2)
        self.txtText2 = QtWidgets.QTextEdit(Form)
        self.txtText2.setObjectName("txtText2")
        self.gridLayout.addWidget(self.txtText2, 2, 0, 1, 1)
        self.btnCrearTabla = QtWidgets.QPushButton(Form)
        self.btnCrearTabla.setObjectName("btnCrearTabla")
        self.gridLayout.addWidget(self.btnCrearTabla, 4, 0, 1, 2)
        self.txtText3 = QtWidgets.QTextEdit(Form)
        self.txtText3.setObjectName("txtText3")
        self.gridLayout.addWidget(self.txtText3, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.retranslateUi(Form)
        self.btnCargarArchivo.clicked.connect(Form.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ventana  Principal (main.py)"))
        self.btnCargarArchivo.setText(_translate("Form", "Cargar Archivo"))
        self.btnCrearMapa.setText(_translate("Form", "Crear Mapa"))
        self.btnCrearTabla.setText(_translate("Form", "Crear Tabla"))
        self.label.setText(_translate("Form", "Nodo Origen"))
        self.label_2.setText(_translate("Form", "Nodo Destino"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
