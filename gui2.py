from tkinter import  filedialog, Text
import os
import matplotlib.pylab as pl
from matplotlib import collections  as mc
import f
import plot

class Ponto:
    def __init__(self, x,y,w):
        self.x = x
        self.y = y
        self.w = w

# funcao para ler pontos de um arquivo
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


print("Escolha a opção desejada")
opcao = 0
while opcao != 5:
    print(''' 
        [ 1 ] Escolher arquivo de pontos
        [ 2 ] Gerar árvore geradora mínima
    ''')
    opcao = int(input("Escolha uma opção "))
    if opcao == 1:
        pontos = lerPontos()
    elif opcao == 2:
        arestas = f.primAlg(pontos)
        plot.plotar(arestas)





