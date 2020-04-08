import os
from tkinter import  filedialog, Text
from Ponto import *


# funcao para ler pontos de um arquivo através de uma interface gráfica
def lerPontos():
    raiz = os.getcwd()
    fileName = filedialog.askopenfilename(initialdir="${raiz}", title="Selecione um arquivo",
    filetypes=(("text", "*.txt"),))
    #os.chdir(raiz + "/TeseAlgoritmos/corretos/") #Muda a pasta raiz para esta (comentar/modificar essa linha caso o código não pegue)
    pontos = []
    with open(fileName, "r") as f:
        for l in f:
            row = l.split()
            p = Ponto(float(row[0]),float(row[1]), float(row[2]))
            pontos.append(p)
    return pontos

# funcao para ler pontos de um arquivo através de seu diretório
def readPontos(fileName):
    pontos = []
    with open(fileName, "r") as f:
        for l in f:
            row = l.split()
            p = Ponto(float(row[0]),float(row[1]), float(row[2]))
            pontos.append(p)
    return pontos