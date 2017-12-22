# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
import random

tabuleiro =[
    [1,1,1],
    [1,1,1],
    [1,1,1]]

def nome():
    nome = str(input('Qual seu nome? \n'))
    return nome
    
def solicitaSimboloDoHumano():
    s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) \n'))
    while s != 'X' and s != 'O':
        print('Insira um símbolo válido.')
        s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) '))
    if s == 'X':
        computador = 'O'
    else:
        computador = 'X'
    return

def sorteioPrimeiraJogada(nome):
    j1 = nome
    j2 = 'Computador'
    sort = random.randint(0,1)
    if sort == 1:
        return print ('Vencedor do sorteio para início do jogo: %s' % j1)
    if sort == 0:
        return print ('Vencedor do sorteio para início do jogo: %s' % j2)
    
def JogadaHumana(nome):
    c= int(input('Qual a sua jogada, %s? ' % nome))
    x = c // 10
    y = c % 10
    tabuleiro [x][y] = b
    return

def validaJogada(tabuleiro) :
    linha = [0,1,2]
    coluna = [0,1,2]
    jogadapossivel = False
    for i in linha :
        for j in coluna :
            k = str(i) + '-' + str(j)
            if not bool(tabuleiro[k]) :
                return True
    return jogadapossivel

def verificaVencedor(s, tabuleiro):
    if True:
        if tabuleiro[0][0] == s and tabuleiro[0][1] == s and tabuleiro[0][2] == s:
            return print('Vencedor: %s' % )
        if tabuleiro[1][0] == s and tabuleiro[1][1] == s and tabuleiro[1][2] == s:
            return print('Vencedor: %s' % )
        if tabuleiro[2][0] == s and tabuleiro[2][1] == s and tabuleiro[2][2] == s:
            return print('Vencedor: %s' % )
        if tabuleiro[0][0] == s and tabuleiro[1][0] == s and tabuleiro[2][0] == s:
            return print('Vencedor: %s' % )
        if tabuleiro[0][1] == s and tabuleiro[1][1] == s and tabuleiro[2][1] == s:
            return print('Vencedor: %s' % )
        if tabuleiro[0][2] == s and tabuleiro[1][2] == s and tabuleiro[2][2] == s:
            return print('Vencedor: %s' % )
        if tabuleiro[0][0] == s and tabuleiro[1][1] == s and tabuleiro[2][2] == s:
            return print('Vencedor: %s' % )
        if tabuleiro[0][2] == s and tabuleiro[1][1] == s and tabuleiro[2][0] == s:
            return print('Vencedor: %s' % )
    else:
        return print('Deu Velha!')
    


'''def determineVictory(board):
    rows = ['top','mid','low']
    cols = ['L','M','R']
    # se uma linha tiver todas as colunas iguais é vitoria
    for r in rows :
        col1 = str(r)+'-L'
        col2 = str(r)+'-M'
        col3 = str(r)+'-R'
        if board[col1] == board[col2] == board[col3] and bool(board[col1]) :
            return board[col3]
    # se uma coluna tiver todas as linhas iguais é vitoria
    for c in cols :
        row1 = 'top-'+str(c)
        row2 = 'mid-'+str(c)
        row3 = 'low-'+str(c)
        if board[row1] == board[row2] == board[row3] and bool(board[row1]) :
            return board[row3]
    # se houver uma diagonal com todas iguais então é vitoria
    middle = 'mid-M';
    sel1, sel2 = str(rows[0]+'-'+cols[2]), str(rows[2]+'-'+cols[0])
    if board[middle] == board[sel1] == board[sel2] :
       return board[middle]
    sel1, sel2 = str(rows[0]+'-'+cols[0]), str(rows[2]+'-'+cols[2])
    if board[middle] == board[sel1] == board[sel2] :
       return board[middle]
    return False'''
    
'''def jogada_pc():
    j1 =
    j2 = 
    sort = random.randint(0,1)
    if sort == 1:
        return
    if sort == 0:
        return'''





def mostrarTabuleiro(tabuleiro) : 
    print((tabuleiro[0] [0])+'|'+(tabuleiro[0] [1])+'|'+(tabuleiro[0] [2]))
    print('')
    print((tabuleiro[1] [0])+'|'+(tabuleiro[1] [1])+'|'+(tabuleiro[1] [2]))
    print('')
    print((tabuleiro[2] [0])+'|'+(tabuleiro[2] [1])+'|'+(tabuleiro[2] [2]))
    return


