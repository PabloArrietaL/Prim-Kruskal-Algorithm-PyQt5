from tabulate import tabulate
import pandas as pd

def table(nodos):
    nodos = nodos.values
    n = len(nodos[0])
    n_nodos = ['-']
    f_nodos = []
    for i in range(n):
        n_nodos.append("{}".format(i+1))
        f_nodos.append(i+1)
    diccionario = {}

    for i in range(len(n_nodos)):
        if(i==0):
            diccionario[n_nodos[i]] = f_nodos
        else:
            diccionario[n_nodos[i]] = nodos[i-1]

    return(tabulate(diccionario,headers='keys'))