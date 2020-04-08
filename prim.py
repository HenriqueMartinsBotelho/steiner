from scipy.spatial import distance
import math
import numpy as np
import matplotlib.pylab as pl
from matplotlib import collections  as mc 
import os

'''
    Função de ponderação usada no algoritmo de Prim.
    Recebe dois pontos e retorna a média aritmética de seus pesos.
'''

def w(p1,p2):
    return distance.euclidean((p1.x,p1.y),(p2.x,p2.y))*(p1.w + p2.w)/2

'''
    Recebe uma lista de pontos da Classe Ponto e retorna uma lista de aresta
    onde cada aresta é formada por dois Pontos.
'''
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