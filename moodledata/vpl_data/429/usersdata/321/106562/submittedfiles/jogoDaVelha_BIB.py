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
    
def JogadaHumana(nome,b):
    c= int(input('Qual a sua jogada, %s? ' % nome))
    x = c // 10
    y = c % 10
    if validaJogada(nome,tabuleiro,x,y,b):
        tabuleiro[x][y]= ' '+b+' '
        return True
    else:
        return False

def jogadaComputador(computador):
    linha = random.randint(0,2)
    coluna= random.randint(0,2)
    if validaJogada('',tabuleiro,linha,coluna,computador):
        tabuleiro[linha][coluna]= computador
        return True
    else:
        return False

def mostrarTabuleiro() : 
    print(tabuleiro[0][0]+'|'+tabuleiro[0][1]+'|'+tabuleiro[0][2])
    print(tabuleiro[1][0]+'|'+tabuleiro[1][1]+'|'+tabuleiro[1][2])
    print(tabuleiro[2][0]+'|'+tabuleiro[2][1]+'|'+tabuleiro[2][2])
    
def validaJogada(nome,tabuleiro,l,c,s) :
    jogadapossivel = False 
    if not tabuleiro[l][c]=='   ':
        if nome!='':
            print('OPS!!! Essa jogada não está disponível. Tente novamente!')
            return False
        else:
           jogadaComputador(s)
    else:
        return True
    
def verificaVencedor(s,tabuleiro,nome):
    if True:
        if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] and (not bool(tabuleiro[0][0])) :
            w= tabuleiro [0][0]
            if w==s:
                print('Vencedor: %s' %nome)
                return False
            else:
                print('Vencedor: Computador')
                return False
        if tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] and not bool (tabuleiro[1][0]):
            w= tabuleiro [1][0]
            if w==s:
                print('Vencedor: %s' %nome)
                return False
            else:
                print('Vencedor: Computador')
                return False
        if tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] and not bool (tabuleiro[2][0]):
            w= tabuleiro [2][0]
            if w==s:
                print('Vencedor: %s' %nome)
                return False
            else:
                print('Vencedor: Computador')
                return False
        if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] and not bool (tabuleiro[0][0]):
            w= tabuleiro [0][0]
            if w==s:
                print('Vencedor: %s' %nome)
                return False
            else:
                print('Vencedor: Computador')
                return False
        if tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] and not bool (tabuleiro[0][1]):
            w= tabuleiro [0][1]
            if w==s:
                print('Vencedor: %s' %nome)
                return False
            else:
                print('Vencedor: Computador')
                return False
        if tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] and not bool (tabuleiro[0][2]):
            w= tabuleiro [0][2]
            if w==s:
                print('Vencedor: %s' %nome)
                return False
            else:
                print('Vencedor: Computador')
                return False
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and not bool (tabuleiro[0][0]):
            w= tabuleiro [0][0]
            if w==s:
                print('Vencedor: %s' %nome)
                return False
            else:
                print('Vencedor: Computador')
                return False
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and not bool (tabuleiro[0][2]):
            w= tabuleiro [0][2]
            if w==s:
                print('Vencedor: %s' %nome)
                return False
            else:
                print('Vencedor: Computador')
                return False
    else:
        print('Deu Velha!')
        return False

  
    
    
    

