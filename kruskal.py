import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

base = dict()
ord = dict()   

def make_set(v):
    base[v] = v
    ord[v] = 0

def find(v):
    if base[v] != v:
        base[v] = find(base[v])
    return base[v]

def union(u, v):
    v1 = find(u)
    v2 = find(v)
    if v1 != v2:
        if ord[v1] > ord[v2]:
            base[v2] = v1 
        else:
            base[v1] = v2
            if ord[v1] == ord[v2]: 
                ord[v2] += 1

def kruskal_alg(graph):
    mst = []
    for v in graph['vertices']:
        make_set(v)
    edges = list(graph['edges'])
    edges.sort()
    for e in edges:
        _, u, v = e
        if find(u) != find(v):
            union(u, v)
            mst.append(e)
    return mst 

def data_div_nr(n,data):
    result=[]
    weight = []
    for i in range(n):
        for j in range(n):
            if(data[i][j]!=0):
                aux = tuple((j+1, i+1))
                if aux not in result:
                    result.append((i+1,j+1))            
                    weight.append(data[i][j])
    return result,weight

def kruskal(data):
    data = data.values
    n = len(data[0])
    result=[]
    weight = []
    nodes = [i+1 for i in range(n)]
    result, weight = data_div_nr(n,data)
    index = 0
    values = []
    for tupla in result:
        aux1 = list(tupla)
        aux1.insert(0,weight[index])
        values.append(aux1)
        index+=1
    graph = {
        'vertices': nodes,
        'edges': values}
    k = list(kruskal_alg(graph))
    new_weight = []
    new_nodes = []
    m = len(k)
    for i in range(m):
        aux = list(k[i])
        new_weight.append(aux[0])
        new_nodes.append(aux[1:])

    G = nx.Graph()
    colors = []
    for i in range(len(new_weight)):
        nodo = list(new_nodes[i])
        G.add_edge(nodo[0],nodo[1], color='red', weight=new_weight[i])
        colors.append('red')

    pos = nx.circular_layout(G)
    edge_labels = { (u,v): d['weight'] for u,v,d in G.edges(data=True)}
    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels )
    nx.draw(G,pos,edge_color=colors)
    plt.title("KRUSKAL GRAPH")
    plt.axis('off')
    plt.show()
    return (sum(new_weight))