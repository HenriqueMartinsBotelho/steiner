import click
import readFile
import prim
import plot
import showcross
import geraPontos
import noCross

arestas = []

@click.group('arquivo')
def arquivo():
    ...


@arquivo.command('arq', help='Comando com opções para rodar em um arquivo de pontos')
@click.argument('caminho')
@click.option(
    '-m', '-mst', 'mst', is_flag=True,
    help='Executa algoritmo de Prim'
)
@click.option(
    '-n', '-nocross', 'nocross', is_flag=True,
    help='Executa algoritmo Nocross'
)

@click.option(
    '-s', '-show', 'show', is_flag=True,
    help='Executa algoritmo Showcross'
)

def arq(caminho, mst, nocross, show):
    #if caminho:
    pontos = readFile.readPontos(caminho)
    if mst:
        arestas = prim.primAlg(pontos)
        plot.plotar(arestas, [])
    if nocross:
        arestas = prim.primAlg(pontos)
        noCross.noCrossAlg(arestas)
    if show:
        arestas = prim.primAlg(pontos)
        showcross.showCrossAlg(arestas)



@arquivo.command('gera')
@click.argument('nome', type=click.STRING)
@click.argument('n', type=click.INT)
@click.argument('p', type=click.BOOL)


def gera(nome, n, p=False):
    '''Comando para gerar arquivos de pontos

    Digite primeiro o nome do arquivo depois o número de pontos de pois 1 se quiser gerar com pesos
    ou 0 se quiser gerar sem pesos.

    Ex: python main.py gera exemplos/pontos 100 1   Gera um arquivo chamado ponto.txt com 100 pontos e com pesos 
    '''
    geraPontos.gerar(nome, n, p)


arquivo()