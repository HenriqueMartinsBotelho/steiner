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
#root.geometry("1024x728+200+200")
root['bg'] = "blue"


# ================================================================================================== #

tem_pesos = tk.IntVar()

# =================================================================================================== 

def lerPontos():
    raiz = os.getcwd()
    fileName = filedialog.askopenfilename(initialdir="${raiz}", title="Selecione um arquivo",
    filetypes=(("text", "*.txt"),))
    label1.config(text=fileName)

def mst(diretorio):
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

# BOTÂO LER ARQUIVO
openFile = tk.Button(root, text="Abrir Arquivos", padx=10, pady=5, fg="white", bg="black", command=lerPontos)

# BOTÂO PRIM
prim = tk.Button(root, text="Gerar MST", padx=10, pady=5, fg="white", bg="black", command=lambda:mst(label1.cget("text")))

# LABEL DIRETÓRIO ARQUIVO
label1 = tk.Label(
    root,
    text="",
    font="Arial 14",
    bd=1,
    relief="flat",
    width="50"
)

#BTN gerar arquivos
gerarArquivos = tk.Button(root, text="Gerar Arquivos", padx=10, pady=5, fg="white", bg="black", command=lambda:gerar(tem_pesos.get()))

#Input quantidade de arquivos
qntArquivos = tk.Entry(root, width="20")

#checkbox pesos
checkPesos = tk.Checkbutton(root, text="Pontos com pesos?", variable=tem_pesos)


# =================================================================================================== #


# Posição dos elementos
openFile.grid(row=0, column=0)
label1.grid(row=0, column=1)
prim.grid(row=0, column=2)
gerarArquivos.grid(row=1, column=0)
qntArquivos.grid(row=1, column=1, sticky="W")
checkPesos.grid(row=1, column=2)

root.mainloop(); 