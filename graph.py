import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def graph(data):
    data = data.values
    n = len(data[0])
    result=[]
    weight = []
    for i in range(n):
        for j in range(n):
            if(data[i][j]!=0):
                aux = tuple((j+1, i+1))
                if aux not in result:
                    result.append((i+1,j+1))            
                    weight.append(data[i][j])
    G = nx.Graph()
    for i in range(len(weight)):
        nodo = result[i]
        G.add_edge(nodo[0],nodo[1], weight=weight[i])
    pos = nx.circular_layout(G)
    edge_labels = { (u,v): d['weight'] for u,v,d in G.edges(data=True)}
    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    plt.title("UNGUIDED GRAPH")
    plt.axis('off')
    plt.show()