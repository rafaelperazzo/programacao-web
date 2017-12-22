# -*- coding: utf-8 -*-
'''
# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
import random
inicio = ['computador','nome']
inicio_sorteio = [1,1]
num_inicio = len(inicio)

def sorteio (x):
    sorteado = 1
    if sorteado in inicio_sorteio:
        return inicio_sorteio.index
'''
def makeBoard() :
    theBoard = {};
    rows = ['top','mid','low']
    cols = ['L','M','R']
    for r in rows :
        for c in cols :
            key = str(r) + '-' + str(c)
            theBoard.setdefault(key,False)
    print('DEBUG: '+str(theBoard))
    return theBoard

def printCell(cell) :
    if cell : 
        return ' '+str(cell)+' '
    else :
        return '   '

def showBoard(board) : 
    print(printCell(board['top-L'])+'|'+printCell(board['top-M'])+'|'+printCell(board['top-R']))
    print('-----------')
    print(printCell(board['mid-L'])+'|'+printCell(board['mid-M'])+'|'+printCell(board['mid-R']))
    print('-----------')
    print(printCell(board['low-L'])+'|'+printCell(board['low-M'])+'|'+printCell(board['low-R']))