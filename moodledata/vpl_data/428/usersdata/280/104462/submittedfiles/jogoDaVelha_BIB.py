# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
def tabuleiro():
    matriz = (['00 |','01 ','|02 '],['10 |','11 ','|12 '],['20 |','21 ','|22 '])
    for i in range(3):
        for j in range(3):
            print(' '+matriz[i][j],end = '')
        print('\n')
def tabuleirob():
    matriz = ([' |',' ','| '],[' |',' ','| '],[' |',' ','| '])
    for i in range(3):
        for j in range(3):
            print(' '+matriz[i][j],end = '')
        print('\n')
def jogada(p,j):
    if p == '00':
        matriz[0][0] = j
    elif p == '01':
        matriz[0][1] = j
    elif p == '02':
        matriz[0][2] = j
    elif p == '10':
        matriz[1][0] = j
    elif p == '11':
        matriz[1][1] = j
    elif p == '12':
        matriz[1][2] = j
    elif p == '20':
        matriz[2][0] = j
    elif p == '21':
        matriz[2][1] = j
    elif p == '22':
        matriz[2][2] = j
