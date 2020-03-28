from scipy.spatial import distance
import math
import numpy as np
import pylab as pl
from matplotlib import collections  as mc
import os

class Ponto:
    def __init__(self, x,y,w):
        self.x = x
        self.y = y
        self.w = w
    


def PontosDoArquivo(diretorio):
    pontos = []
    with open(diretorio, "r") as f:
        for l in f:
            row = l.split()
            p = Ponto(float(row[0]),float(row[1]), float(row[2]))
            pontos.append(p)
    return pontos


a = PontosDoArquivo("/home/henrique/dev/steiner/cruzamento1.txt")

for i in a:
    print(i.x)
'''
pontos = pontosFromFile("cruzamento1.txt")
arestas = prim(pontos)
arestas = convertePrim(arestas)
lc = mc.LineCollection(arestas, linewidths=1)
fig, ax = pl.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.margins(0.1)
pl.show()'''