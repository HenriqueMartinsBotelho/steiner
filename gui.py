import tkinter as tk
from tkinter import  filedialog, Text
import os
from scipy.spatial import distance
import math
import numpy as np
import matplotlib.pylab as pl
from matplotlib import collections  as mc
import f
import plot

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
    pontos = f.PontosDoArquivo(diretorio)
    arestas = f.primAlg(pontos)
    plot.plotar(arestas)
    '''arestas = f.convertePrim(arestas)
    lc = mc.LineCollection(arestas, linewidths=1)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    pl.show()
'''
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

# GERAR ARQUIVO PARA O EVOLVER
gerarArquivoEvolver = tk.Button(root, text="Gerar Arquivo para o Evolver", padx=10, pady=5, fg="white", bg="black", command=lambda:f.gerarEvolver())

# MOSTRAR INTERSECÇÕES
mostrarInterseccoes = tk.Button(root, text="Mostrar Intersecções", padx=10, pady=5, fg="white", bg="black", command=lambda:f.mostrarInter())

# REMOVER INTERSECÇÕES
removerInterseccoes = tk.Button(root, text="Remover Intersecções", padx=10, pady=5, fg="white", bg="black", command=lambda:f.removerInter())


'''
#BTN gerar arquivos
gerarArquivos = tk.Button(root, text="Gerar Arquivos", padx=10, pady=5, fg="white", bg="black", command=lambda:f.gerar(tem_pesos.get()))

#Input quantidade de arquivos
qntArquivos = tk.Entry(root, width="20")

#checkbox pesos
checkPesos = tk.Checkbutton(root, text="Pontos com pesos?", variable=tem_pesos)
'''

# =================================================================================================== #


# Posição dos elementos
openFile.grid(row=0, column=0, sticky="W")
label1.grid(row=0, column=1, sticky="W")
prim.grid(row=0, column=2, sticky="W")
gerarArquivoEvolver.grid(row=0,column=3, sticky="W")
mostrarInterseccoes.grid(row=1,column=0, sticky="W")
removerInterseccoes.grid(row=1,column=1, sticky="W")

'''gerarArquivos.grid(row=1, column=0)
qntArquivos.grid(row=1, column=1, sticky="W")
checkPesos.grid(row=1, column=2)'''

root.mainloop(); 