# FALTA implementar a função ehFolha

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
    

''' Recebe uma aresta "e" e a encurta do jeito certo, i.e encolhe 
    na direção da folha '''
def encurtaAresta(e):
    a = e[0].x
    b = e[0].y
    c = e[1].x
    d = e[1].y
    if ehFolha(c,d): #Uso a equação vetoria (a + b) + k(c - a; d - b) para achar um ponto na aresta
        ne = [Ponto(a,b), Ponto(c + 0.9*(a-c), d + 0.9*(b-d) )]
    else:
        ne = [Ponto(c + 0.9*(a-c), d + 0.9*(b-d) ), Ponto(c,d)]
    return ne


'''
 Recebe duas arestas "e1" e "e2" que se cruzam e diminui "e2" transformando
 em "e2Short" tal que "e1" e "e2Short" não mais se cruzam. Então retorna
 [e1, e2Short]. 
'''
def removeCruzamento(e1, e2):
    while (intersect(e1[0], e1[1], e2[0], e2[1])):
        e2 = encurtaAresta(e2)
    return [e1, e2]


'''
Remove todos os cruzamentos e retorna as novas arestas
'''
def removeCruzamentoS(cruzamento2):
    novasArestas = []
    for item in cruzamento2:
        rc = removeCruzamento(item[0], item[1])
        novasArestas.append(rc)
    return novasArestas

def noCrossAlg(arestas):
    cruzamentos = []
    remover = []
    for e1 in arestas:
        for e2 in arestas:
            if e1 != e2:
                if intersect(e1[0], e1[1], e2[0], e2[1]):
                    if [e1, e2] not in cruzamentos and [e2, e1] not in cruzamentos:
                        cruzamentos.append([e1, e2])
                        remover.append(e2)
    for a in remover:
        arestas.remove(a)
    novasArestas = removeCruzamentoS(cruzamentos)
    semCruzamento = []
    for item in novasArestas:
        semCruzamento.append(item[0])
        semCruzamento.append(item[1])

    plot.plotar(arestas, semCruzamento, 'b')
