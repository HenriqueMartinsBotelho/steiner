import click
import readFile
import prim
import plot
import showcross

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
        click.echo("chamar nocross")
    if show:
        arestas = prim.primAlg(pontos)
        showcross.showCrossAlg(arestas)



@arquivo.command('gerar',  help='Comando com opções para gerar arquivos com pontos')
@click.argument('n', type=click.INT)
@click.option(
    '-peso', 'peso', is_flag=True,
    help='Gera pontos com pesos',
)
def gerar(n, peso):
    click.echo(n)


arquivo()