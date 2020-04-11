import random
import math

def gerar(nome, n, peso=True):
    pts = []
    arquivo = open(nome + '.txt', 'w')
    for i in range(n):
        x = 100 * random.random()
        y = 100 * random.random()
        if peso == True:
            p = random.randint(1,77)
        else:
            p = 1
        x = str(x)
        y = str(y)
        p = str(p)
        arquivo.write(str(x + ' ' + y + ' ' + p))
        arquivo.write('\n')
        pts = []
    arquivo.close
