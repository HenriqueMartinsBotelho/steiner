import keyboard
import time
import curses
import tkinter
from tkinter import  filedialog, Text
import os
import matplotlib.pylab as pl
from matplotlib import collections  as mc
import f
import plot

root = tkinter.Tk()
root.withdraw()

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






menu = ['1 - Escolher pontos', '2 - Gerar MST', '5 - SAIR']

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.getch()
            # if user selected last row, exit the program
            if current_row == len(menu)-1:
                break
            elif current_row == 0:
                pontos = lerPontos()
            elif current_row == 1:
                arestas = f.primAlg(pontos)
                plot.plotar(arestas)
            else:
                print("Hi")

        print_menu(stdscr, current_row)


curses.wrapper(main)



"""
def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row_idx = 0

    print_menu(stdscr, current_row_idx)

    while 1:
        key = stdscr.getch()
        stdscr.clear()
        
        if keyboard.read_key() == 'up' and current_row_idx > 0:
            current_row_idx -= 1
        elif keyboard.read_key() == 'down' and current_row_idx < len(menu) - 1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.refresh()
            stdscr.getch()
            if current_row_idx == len(menu) - 1:
                break
            elif current_row_idx == 0:
                pontos = lerPontos()
            elif current_row_idx == 1:
                arestas = f.primAlg(pontos)
                plot.plotar(arestas)
            stdscr.refresh()
        stdscr.refresh()


        
        print_menu(stdscr, current_row_idx)
        stdscr.refresh()

curses.wrapper(main)

"""











"""



print("Escolha a opção desejada")
opcao = 0
while opcao != 5:
    print(''' 
        [ 1 ] Escolher arquivo de pontos
        [ 2 ] Gerar árvore geradora mínima
        [ 5 ] Fechar o programa
    ''')
    opcao = int(input("Escolha uma opção "))
    if opcao == 1:
        pontos = lerPontos()
        root.destroy()
    elif opcao == 2:
        arestas = f.primAlg(pontos)
        plot.plotar(arestas)



"""