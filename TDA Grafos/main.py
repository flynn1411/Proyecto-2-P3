import sys
from main_ui import *
from PyQt5.QtWidgets import *
class Ventana(QWidget):
	def __init__(self,parent = None):
		QtWidgets.QWidget. __init__(self,parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.ui.btnCargarArchivo.clicked.connect(self.CargarArchivo)
		self.ui.txtText2.setText("Nodo Origen")
		self.ui.txtText3.setText("Nodo Destino")
	def CargarArchivo(self):
		#filename = open("memoria.txt","r")
		#datos = filename.read()
		#print(datos)
		#self.ui.txtText1.setText(datos)
		#datos = filename
		self.openFileNameDialog()
		self.saveFileDialog()
		self.show()
	
	def openFileNameDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		filename, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()","","All Files (*);;Python Files (*.py)", options = options)
		directorio = filename
		archivo = open(directorio,"r")
		content = archivo.read()
		print(content)
		self.ui.txtText1.setText(content)

	def saveFileDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		filename, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()","","All Files (*);;Python Files (*.py)", options = options)

if __name__ == "__main__":
	mi_aplicacion = QApplication(sys.argv)
	mi_app = Ventana()
	mi_app.show()
	sys.exit(mi_aplicacion.exec_())
