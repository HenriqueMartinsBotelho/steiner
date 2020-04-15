def printAresta(e1):
    print([(e1[0].x, e1[0].y), (e1[1].x, e1[1].y)])

def formataAresta(e1):
    return str(([(e1[0].x, e1[0].y), (e1[1].x, e1[1].y)]))

def saveArestas(arestas, fileName):
    
    with open(f'arestas/{fileName}', 'w') as fileArestas:
        for item in arestas:
            fileArestas.write(formataAresta(item))
            fileArestas.write('\n')
        
