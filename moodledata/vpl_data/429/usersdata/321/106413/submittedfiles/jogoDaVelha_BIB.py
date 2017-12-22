# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
import random

tabuleiro = [
    ['   ','   ','   '],
    ['   ','   ','   '],
    ['   ','   ','   ']]

def nome():
    nome = str(input('Qual seu nome? \n'))
    return nome
    
def solicitaSimboloDoHumano():
    s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) \n'))
    while s != 'X' and s != 'O':
        print('Insira um símbolo válido.')
        s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) '))
    return s

def sorteioPrimeiraJogada(nome):
    j1 = nome
    j2 = 'Computador'
    sort = random.randint(0,1)
    if sort == 1:
        print ('Vencedor do sorteio para início do jogo: %s' % j1)
    if sort == 0:
        print ('Vencedor do sorteio para início do jogo: %s' % j2)
    return sort
    
def JogadaHumana(nome):
    c= int(input('Qual a sua jogada, %s? ' % nome))
    x = c // 10
    y = c % 10
    return x,y
    
def validaJogada(nome,tabuleiro) :
    jogadapossivel = False
    for i in range(0,3,1):
        for j in range(0,3,1):
            if not bool(tabuleiro[i][j]) :
                return print('OPS!!! Essa jogada não está disponível. Tente novamente!')
            else:
                return True
    return jogadapossivel

def verificaVencedor(s,tabuleiro,nome):
    if True:
        w=0
        if (tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2]):
            w= tabuleiro [0][0]
            if w==s:
                print('Vencedor: %s' %nome)
            else:
                print('Vencedor: Computador')
        if tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] and not boll (tabuleiro[1][0]):
            w= tabuleiro [1][0]
            if w==s:
                print('Vencedor: %s' %nome)
            else:
                print('Vencedor: Computador')
        if tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] and not boll (tabuleiro[2][0]):
            w= tabuleiro [2][0]
            if w==s:
                print('Vencedor: %s' %nome)
            else:
                print('Vencedor: Computador')
        if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] and not boll (tabuleiro[0][0]):
            w= tabuleiro [0][0]
            if w==s:
                print('Vencedor: %s' %nome)
            else:
                print('Vencedor: Computador')
        if tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] and not boll (tabuleiro[0][1]):
            w= tabuleiro [0][1]
            if w==s:
                print('Vencedor: %s' %nome)
            else:
                print('Vencedor: Computador')
        if tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] and not boll (tabuleiro[0][2]):
            w= tabuleiro [0][2]
            if w==s:
                print('Vencedor: %s' %nome)
            else:
                print('Vencedor: Computador')
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and not boll (tabuleiro[0][0]):
            w= tabuleiro [0][0]
            if w==s:
                print('Vencedor: %s' %nome)
            else:
                print('Vencedor: Computador')
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and not boll (tabuleiro[0][2]):
            w= tabuleiro [0][2]
            if w==s:
                print('Vencedor: %s' %nome)
            else:
                print('Vencedor: Computador')
    else:
        return print('Deu Velha!')

def jogadaComputador(computador):
    linha = random.randint(0,2)
    coluna= random.randint(0,2)
    tabuleiro[linha][coluna]= computador
    
    
    
def mostrarTabuleiro() : 
    print(tabuleiro[0][0]+'|'+tabuleiro[0][1]+'|'+tabuleiro[0][2])
    print(tabuleiro[1][0]+'|'+tabuleiro[1][1]+'|'+tabuleiro[1][2])
    print(tabuleiro[2][0]+'|'+tabuleiro[2][1]+'|'+tabuleiro[2][2])  
    
    
    
'''    
    if linha == 1:
        tabuleiro[sort]='O'
    if sort == 2:
        tabuleiro[sort]='O'
    if sort == 3:
        tabuleiro[sort]='O'    
    if sort == 4:
        tabuleiro[sort]='O'
    if sort == 5:
        tabuleiro[sort]='O' 
    if sort == 6:
        tabuleiro[sort]='O'
    if sort == 7:
        tabuleiro[sort]='O'
    if sort == 8:
        tabuleiro[sort]='O'
    if sort == 9:
        tabuleiro[sort]='O'
    print(tabuleiro)        
'''

    
'''    
    print(tabuleiro[0][0]+'|'+tabuleiro[0][1]+'|'+tabuleiro[0][2])
    return

    print('')
    print((tabuleiro[1][0])+'|'+(tabuleiro[1] [1])+'|'+(tabuleiro[1] [2]))
    print('')
    print((tabuleiro[2][0])+'|'+(tabuleiro[2] [1])+'|'+(tabuleiro[2] [2]))
    return
'''
