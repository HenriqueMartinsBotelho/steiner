import tkinter as tk
from tkinter import  filedialog, Text
import os
from scipy.spatial import distance
import math
import numpy as np
import matplotlib.pylab as pl
from matplotlib import collections  as mc
import f


# Converte as arestas para um formato imprimível  
def convertePrim(E):
    arestas = []
    for e in E:
        p1 = (e[0].x, e[0].y)
        p2 = (e[1].x, e[1].y)
        arestas.append([p1,p2])  
    return arestas       



def plotar(arestas):
    arestas = convertePrim(arestas)
    lc = mc.LineCollection(arestas, linewidths=1)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    pl.show()