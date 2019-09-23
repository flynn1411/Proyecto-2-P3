import sys
from main_ui import *
from load import*
from PyQt5.QtWidgets import *
import networkx as nx
import matplotlib.pyplot as plt
import pylab
class Ventana(QWidget):
	def __init__(self,parent = None):
		QtWidgets.QWidget. __init__(self,parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.ui.btnCargarArchivo.clicked.connect(self.CargarArchivo)
		self.ui.btnCrearTabla.clicked.connect(self.creatTable)
		self.ui.btnCrearMapa.clicked.connect(self.CreateMap)
	
	#Crear la tabla hasta la linea 40
	def creatTable(self):
		from creatTable import tablePage
		b = tablePage()
		#Obtener el string de las cajas de texto de la interfaz 
		origin = self.ui.txtText2.toPlainText()
		destination = self.ui.txtText3.toPlainText()

		array = self.actualFile.split('\n')
		loader = Loader()
		loader.load(array)

		#escribir en la tabla 
		b.textEdit.setText(Ventana.pathsToTable("none", loader.G.getAllPaths(origin, destination), origin, destination))
		b.exec_()
	
	def pathsToTable(self,path,origin,destination):

		table = []
		tabs = "-"*(71)
		#titulo de la tabla 
		header = "%s\n\t\tRutas de %s a %s\n%s\n\tPeso\t|\tRutas\n%s" %(tabs , origin , destination , tabs, tabs)
		table.append(header)

		#recorrer el arreglo para agregar sus elementos a la tabla 
		for i in path:
			currentPath = ""
			for v in range (len(i["path"])-1):
				currentPath += ("%s, " %i["path"][v])
			currentPath += i["path"][len(i["path"])-1]

			table.append("\n\t%s\t|\t%s\n%s" %(i["weight"], currentPath,tabs) )
		
		return "".join(table)
		
	def CargarArchivo(self):
		#filename = open("memoria.txt","r")
		#datos = filename.read()
		#print(datos)
		#self.ui.txtText1.setText(datos)
		#datos = filename
		self.openFileNameDialog()
		#self.saveFileDialog()
		self.show()
	
	def openFileNameDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		filename, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()","","All Files (*);;Python Files (*.py)", options = options)
		
		directorio = filename
		archivo = open(directorio,"r")
		content = archivo.read()
		self.ui.txtText1.setText(content)
		self.actualFile = self.ui.txtText1.toPlainText()
		print(self.actualFile)

	def CreateMap(self):
		array = self.actualFile.split('\n')
		loader = Loader()
		loader.load(array)
		G=nx.DiGraph()
		for vertex,edges in loader.G.vertices.items():
		    G.add_node('%s'%vertex)
		    for edge in edges.edges:
		        G.add_node('%s'%edge)
		        G.add_edge('%s'%vertex,'%s'%edge,weight=('%s'%edges.edges[edge]))
		pos=nx.spring_layout(G)
		edge_labels=dict([((u,v,),d['weight'])for u,v,d in G.edges(data=True)])
		nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
		nx.draw_networkx(G,pos,with_labes=True)
		plt.savefig("Grafo.jpg")
		pylab.show()
	

if __name__ == "__main__":
	mi_aplicacion = QApplication(sys.argv)
	mi_app = Ventana()
	mi_app.show()
	sys.exit(mi_aplicacion.exec_())
