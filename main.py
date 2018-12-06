#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
from PyQt5 import uic, QtWidgets, QtCore
from table import table
from graph import graph
from kruskal import kruskal
from prim import prim

qtCreatorFile = "graphic.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        #Aquí van los botones
        self.imp.clicked.connect(self.import_csv)
        self.send.clicked.connect(self.show_table)
        self.graph.clicked.connect(self.show_graph)
        self.kruskal.clicked.connect(self.show_kruskal)
        self.prim.clicked.connect(self.show_prim)
        self.restart.clicked.connect(self.restar_app)
        
    #Aquí van las nuevas funciones
    def import_csv(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '.',"CSV Files (*.csv)")
        if filePath != "":
            self.df = pd.read_csv(str(filePath),header=None,delimiter=';')
        self.send.setEnabled(True)
        self.restart.setEnabled(True)
        self.imp.setEnabled(False)
            
    def show_table(self):
        tab = table(self.df)
        text = "\nMatriz de adyacencia\n"+str(tab)
        self.result.setText(text)
        self.send.setEnabled(False)
        self.graph.setEnabled(True)
        self.kruskal.setEnabled(True)
        self.prim.setEnabled(True)

    def show_graph(self):
        graph(self.df)

    def show_kruskal(self):
        text = kruskal(self.df)
        self.k_weight.setText(str(text))
    
    def show_prim(self):
        text = prim(self.df)
        self.p_weight.setText(str(text))
        
    def restar_app(self):
        self.result.setText("")
        self.p_weight.setText("")
        self.k_weight.setText("")
        self.imp.setEnabled(True)
        self.send.setEnabled(False)
        self.graph.setEnabled(False)
        self.kruskal.setEnabled(False)
        self.prim.setEnabled(False)
        self.restart.setEnabled(False)

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec()