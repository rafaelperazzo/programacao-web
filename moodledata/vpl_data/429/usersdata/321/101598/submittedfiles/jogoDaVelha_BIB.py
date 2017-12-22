# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
import random
inicio = ['computador','nome']
inicio_sorteio = [1,1]
num_inicio = len(inicio)

def sorteio (x):
    sorteado = 1
    while (True):
        sorteado  = random.randint(0,num_inicio-1)
        if sorteado in inicio:
            return inicio.index

tabuleiro = [
    ['','',''],
    ['','',''],
    ['','','']]
   