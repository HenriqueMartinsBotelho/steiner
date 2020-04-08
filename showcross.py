import plot


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

   
## Recebe uma lista de arestas e mostra quais delas cruzam
def showCrossAlg(arestas):
    cruzamentos = []
    for e1 in arestas:
        for e2 in arestas:
            if e1 != e2:
                if intersect(e1[0], e1[1], e2[0], e2[1]):
                    cruzamentos.append(e1)
                    cruzamentos.append(e2)
    plot.plotar(arestas, cruzamentos, 'b')
