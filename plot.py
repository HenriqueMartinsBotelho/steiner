import time
import os
import matplotlib.pylab as pl
from matplotlib import collections  as mc


# Converte as arestas para um formato imprimível  
def convertePrim(E):
    arestas = []
    for e in E:
        p1 = (e[0].x, e[0].y)
        p2 = (e[1].x, e[1].y)
        arestas.append([p1,p2])  
    return arestas       


# Plota as arestas
def plotar(arestas, cruzamentos, cor='b'):
    arestas = convertePrim(arestas)
    cruzamentos = convertePrim(cruzamentos)
    lc = mc.LineCollection(arestas, linewidths=1, colors='b')
    lc2 = mc.LineCollection(cruzamentos, linewidths=1, colors='r') # Coleção de arestas vermelhas generalizar o arestas[0]
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.add_collection(lc2)
    ax.autoscale()
    ax.margins(0.1)
    pl.show()