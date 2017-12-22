# -*- coding: utf-8 -*-
import random
from time import sleep
# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
def tabuleiro():
    matriz = (['00 |','01','| 02 '],['10 |','11','| 12 '],['20 |','21','| 22 '])
    for i in range(3):
        for j in range(3):
            print(' '+matriz[i][j],end = '')
        print('\n')
def tabuleirob(matriz):
    matriz = ([' |',' ','| '],[' |',' ','| '],[' |',' ','| '])
    for i in range(3):
        for j in range(3):
            print(' '+matriz[i][j],end = '')
        print('\n')

def vitoria(j):
    vetor = []
    matriz = [''],[''],['']
    vencedor = ('')
    vetor = str(vetor)
    if j == 9:
        vencedor = 'VELHA'
        #Horizontais
    vetor[0] = matriz[0][0] + matriz[0][1] + matriz[0][2]
    vetor[1] = matriz[1][0] + matriz[1][1] + matriz[1][2]
    vetor[2] = matriz[2][0] + matriz[2][1] + matriz[2][2]
        #Verticais
    vetor[3] = matriz[0][0] + matriz[1][0] + matriz[2][0]
    vetor[4] = matriz[0][1] + matriz[1][1] + matriz[2][1]
    vetor[5] = matriz[0][2] + matriz[1][2] + matriz[2][2]
        #Diagonais
    vetor[6] = matriz[0][0] + matriz[1][1] + matriz[2][2]
    vetor[7] = matriz[0][2] + matriz[1][1] + matriz[2][0]  
    for i in range(len(vetor)):
        if vetor[i] == 'XXX':
            vencedor = 'jogador 1'
        else:
            vencedor = 'jogador 2'
    return vencedor
