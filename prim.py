import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import random
from PyQt5.QtWidgets import QMessageBox

def dic(n,data,weight):
    edges = {}
    for i in range(n):
        aux = []
        for node in data:
            if(i+1==node[0]):
                aux2 = data.index(node)
                aux.append((node[1],weight[aux2]))
        edges[i+1] = aux
    return edges

def prim_al(edges,n):
    n_edges = []
    weight = []
    nod = []
    start = 0
    for _ in range(n-1):
        l_weight = []
        l_node = []
        if (start==0):
            start = random.randint(1,n)
            nod.append(start)
            aux = edges[start]
            aux.sort()
            for tup in aux:
                l_weight.append(tup[1])
                l_node.append(tup[0])
            mini = min(l_weight)
            pos = l_weight.index(mini)
            weight.append(mini)
            finish = l_node[pos]
            nod.append(finish)
            n_edges.append((start,finish))
            start = finish
        else:
            aux = edges[start]
            aux.sort()
            for tup in aux:
                l_weight.append(tup[1])
                l_node.append(tup[0])
            
            for j in nod:
                if (j in l_node):
                    po = l_node.index(j)
                    l_node.remove(j)
                    l_weight.pop(po)
            if(l_node == []):
                pass
            else:
                mini = min(l_weight)
                pos = l_weight.index(mini)
                weight.append(mini)
                n_start = l_node[pos]
                finish = l_node[pos]
                nod.append(finish)
                n_edges.append((start,finish))
                start = n_start
    return weight, n_edges

def data_div(n,data):
    result=[]
    weight = []
    for i in range(n):
        for j in range(n):
            if(data[i][j]!=0):
                result.append((i+1,j+1))            
                weight.append(data[i][j])
    return result,weight


def prim(data):
    data = data.values
    n = len(data[0])
    result,weight = data_div(n,data)
    edges = (dic(n,result,weight))
    new_weights, new_nodes = prim_al(edges,n)
    if(len(new_nodes)<(n-1)):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("ERROR")
        msg.setText("No se encontró una solución adecuada.\nRepita el procedimiento.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
    else:
        G = nx.Graph()
        colors = []
        for i in range(len(new_weights)):
            nodo = new_nodes[i]
            G.add_edge(nodo[0],nodo[1], color='red', weight=new_weights[i])
            colors.append('red')

        pos = nx.circular_layout(G)
        edge_labels = { (u,v): d['weight'] for u,v,d in G.edges(data=True)}
        nx.draw_networkx_nodes(G,pos)
        nx.draw_networkx_edges(G,pos)
        nx.draw_networkx_labels(G,pos)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels )
        nx.draw(G,pos,edge_color=colors)
        plt.title("PRIM GRAPH")
        plt.axis('off')
        plt.show()
        return sum(new_weights)