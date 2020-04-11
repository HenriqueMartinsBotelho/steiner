
import plot
from Ponto import *


def printAresta(e1):
    print([(e1[0].x, e1[0].y), (e1[1].x, e1[1].y)])

def cross_product(p1, p2):
	return p1.x * p2.y - p2.x * p1.y

def direction(p1, p2, p3):
	return  cross_product(p3.subtract(p1), p2.subtract(p1)) 

def intersect(p1, p2, p3, p4):
    d1 = direction(p3, p4, p1)
    d2 = direction(p3, p4, p2)
    d3 = direction(p1, p2, p3)
    d4 = direction(p1, p2, p4)

    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and \
        ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    else:
        return False

#implementar
def ehFolha(p1, p2):
    return False

def encurtaAresta(cruzamentos):
    newEdges = []
    for i in range(len(cruzamentos)):
        if i % 2 == 1:
            p1 = cruzamentos[i][0]
            p2 = cruzamentos[i][1]
            a = p1.x
            b = p1.y
            c = p2.x
            d = p2.y
            if ehFolha(c,d): #Uso a equação vetoria (a + b) + k(c - a; d - b) para achar um ponto na aresta
                ne = [Ponto(a,b), Ponto(c + 0.5*(a-c), d + 0.5*(b-d) )]
            else:
                ne = [Ponto(c + 0.5*(a-c), d + 0.5*(b-d) ), Ponto(c,d)]
            old = [Ponto(cruzamentos[i-1][0].x, cruzamentos[i-1][0].y), Ponto(cruzamentos[i-1][1].x, cruzamentos[i-1][1].y)]
            newEdges.append(old)
            newEdges.append(ne)
    print("==== NOVA LISTA DE ARESTAS ======")
    for e in newEdges:
        printAresta(e)
    return newEdges
    



## Recebe uma lista de arestas e remove os cruzamentos
def noCrossAlg(arestas):
    cruzamentos = []
    for e1 in arestas:
        for e2 in arestas:
            if e1 != e2:
                if intersect(e1[0], e1[1], e2[0], e2[1]):
                    if e1 not in cruzamentos and e2 not in cruzamentos:
                        cruzamentos.append(e1)
                        cruzamentos.append(e2)
    for aresta in cruzamentos:
        printAresta(aresta)
    cruzamentos = encurtaAresta(cruzamentos)
    #teste = encurtaAresta(cruzamentos)
    #for t in teste:
    #    printAresta(t)
    plot.plotar(arestas, cruzamentos, 'b')
