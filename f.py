from scipy.spatial import distance
import math
import numpy as np
import matplotlib.pylab as pl
from matplotlib import collections  as mc 
import os

class Ponto:
    def __init__(self, x,y,w):
        self.x = x
        self.y = y
        self.w = w
    
def w(p1,p2):
    return distance.euclidean((p1.x,p1.y),(p2.x,p2.y))*(p1.w + p2.w)/2

def primAlg(pontos):
    E = []
    NaoEsc = pontos[1:]
    Esc = [pontos[0]]
    while len(Esc) < len(pontos):
        menor = math.inf
        for x in NaoEsc:
            for y in Esc:
                dist = w(x,y)
                if dist < menor:
                    menor = dist
                    xe = x
                    ye = y
                    e = [xe,ye]
        E.append(e)
        NaoEsc.remove(xe)
        Esc.append(xe)
    return E


###### LER PONTOS DE UM ARQUIVO E IMPRIMINDO AS ARESTAS ######

# Converte as arestas para um formato imprimível  
def convertePrim(E):
    arestas = []
    for e in E:
        p1 = (e[0].x, e[0].y)
        p2 = (e[1].x, e[1].y)
        arestas.append([p1,p2])  
    return arestas       

def pontosFromFile(fileName):
    raiz = os.getcwd() #Mostra qual a pasta raiz
    os.chdir(raiz + "/TeseAlgoritmos/corretos/") #Muda a pasta raiz para esta (comentar/modificar essa linha caso o código não pegue)
    pontos = []
    with open(fileName, "r") as f:
        for l in f:
            row = l.split()
            p = Ponto(float(row[0]),float(row[1]), float(row[2]))
            pontos.append(p)
    return pontos


def PontosDoArquivo(diretorio):
    pontos = []
    with open(diretorio, "r") as f:
        for l in f:
            row = l.split()
            p = Ponto(float(row[0]),float(row[1]), float(row[2]))
            pontos.append(p)
    return pontos



def gerar(tem_pesos):
    print("OK")
    print(tem_pesos)



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
