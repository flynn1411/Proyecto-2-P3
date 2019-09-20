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
        Form.resize(497, 564)
        self.txtText1 = QtWidgets.QTextEdit(Form)
        self.txtText1.setGeometry(QtCore.QRect(30, 20, 431, 211))
        self.txtText1.setObjectName("txtText1")
        self.txtText2 = QtWidgets.QTextEdit(Form)
        self.txtText2.setGeometry(QtCore.QRect(30, 250, 191, 91))
        self.txtText2.setObjectName("txtText2")
        self.txtText3 = QtWidgets.QTextEdit(Form)
        self.txtText3.setGeometry(QtCore.QRect(270, 250, 191, 91))
        self.txtText3.setObjectName("txtText3")
        self.btnCargarArchivo = QtWidgets.QPushButton(Form)
        self.btnCargarArchivo.setGeometry(QtCore.QRect(50, 360, 151, 71))
        self.btnCargarArchivo.setObjectName("btnCargarArchivo")
        self.btnCrearMapa = QtWidgets.QPushButton(Form)
        self.btnCrearMapa.setGeometry(QtCore.QRect(280, 360, 151, 71))
        self.btnCrearMapa.setObjectName("btnCrearMapa")
        self.btnCrearTabla = QtWidgets.QPushButton(Form)
        self.btnCrearTabla.setGeometry(QtCore.QRect(160, 450, 151, 71))
        self.btnCrearTabla.setObjectName("btnCrearTabla")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.btnCrearTabla.clicked.connect(self.creatTable)
	

    def creatTable(slef):
        from creatTable import tablePage
        #instancia 
        b = tablePage()
        tabla = "La tabla del trafico \n ---------------------- \n\t%s\t|\t%s " %("pene" , "12in")
        b.textEdit.setText(tabla)
        b.exec_()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ventana  Principal (main.py)"))
        self.btnCargarArchivo.setText(_translate("Form", "Cargar Archivo"))
        self.btnCrearMapa.setText(_translate("Form", "Crear Mapa"))
        self.btnCrearTabla.setText(_translate("Form", "Crear Tabla"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
