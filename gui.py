import tkinter as tk
from tkinter import  filedialog, Text
import os
from scipy.spatial import distance
import math
import numpy as np
import pylab as pl
from matplotlib import collections  as mc
from prim import *

root = tk.Tk()

# =================================================================================================== 

def lerPontos():
    raiz = os.getcwd()
    fileName = filedialog.askopenfilename(initialdir="${raiz}", title="Selecione um arquivo",
    filetypes=(("text", "*.txt"),))
    label1.config(text=fileName)

def mst():
    diretorio = label1.cget("text")
    pontos = PontosDoArquivo(diretorio)
    arestas = primAlg(pontos)
    arestas = convertePrim(arestas)
    lc = mc.LineCollection(arestas, linewidths=1)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    pl.show()

# =================================================================================================== #

# CANVAS
canvas = tk.Canvas(root, bg="#263D42")
canvas.pack()

# BOTÂO LER ARQUIVO
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="black", command=lerPontos)
openFile.pack()

# BOTÂO PRIM
prim = tk.Button(root, text="Gerar MST", padx=10, pady=5, fg="white", bg="black", command=mst)
prim.pack()
# LABEL DIRETÓRIO ARQUIVO
label1 = tk.Label(
    root,
    text="",
    font="Arial 14",
    bd=1,
    relief="flat"
)
label1.pack()






root.mainloop(); 