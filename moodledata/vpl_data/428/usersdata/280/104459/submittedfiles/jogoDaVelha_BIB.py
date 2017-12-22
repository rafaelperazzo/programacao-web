# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
def tabuleiro():
    matriz = (['00 |','01 ','|02 '],['10 |','11 ','|12 '],['20 |','21 ','|22 '])
    for i in range(3):
        for j in range(3):
            print(' '+matriz[i][j],end = '')
        print('\n')
def tabuleirob():
    matriz = (['|',' ',' '],[' |',' ','| '],[' |',' ','| '])
    for i in range(3):
        for j in range(3):
            print(' '+matriz[i][j],end = '')
        print('\n')
