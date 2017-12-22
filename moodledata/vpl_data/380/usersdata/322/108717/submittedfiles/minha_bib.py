# -*- coding: utf-8 -*-
import random

tabuleiro = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
simbolos = ['X', 'O']
jogadasPossiveis = ['O','1','2']

def solicitaSimboloDoHumano():
    s = ''
    while True:
        s = input('\nQual símbolo você deseja utilizar no jogo? ')
        if not(s in simbolos):
            print('\nPor favor, selecione um símbolo válido: X ou O')
            continue
        if s == simbolo [0]:
            return 0
        else:
             return 1
             
def sorteioPrimeiraJoagada(nome):
    r = random.randint(0,1)
    if r == 0:
        print('\nVencedor do sorteio para início do jogo: %s' % 'Computador')
    else:
        print('\nVencedor do sorteio para início do jogo: %s' % nome)
    return r
    
def validaJoagada(xy):
    if len(xy) != 2:
        return False
    if not xy[0] in joagadasPossiveis:
        return False
    if not xy[1] in joagadasPossiveis:
        return False
    x = int(xy[0])
    y = int(xy[1])
    
    if not tabuleiro[x][y] == ' ':
        return False
    return True
    
def jogadaHumana(nome, simboloIndex):
    while True:
        jogada = input('\nQual a sua joagada, %? '% nome)
        xy = jogada.split(' ')
        if validaJoagada(xy):
            x = int(xy[0])
            y = int(xy[1])
            tabuleiro[x][y] = simbolos[simboloIndex]
            break
        else:
            print('\nOPS!!! Essa joagada não está disponível. Tente novamente!')
            
def jogadaComputador(simboloIndex):
    while True:
        x = random.randint(0,2)
        y = random.randint(0,2)
        if tabuleiro[x][y] ==' ':
            tabuleiro[x][y] = simbolos[not simboloIndex]
            break
            
def mostrarTabuleiro():
    print('      ')
    print(' '+ tabuleiro[0][0]+' '+tabuleiro[0][1]+' '+tabuleiro[0][2]+' ')
    print('      ')
    print(' '+ tabuleiro[1][0]+' '+tabuleiro[1][1]+' '+tabuleiro[1][2]+' ')
    print('      ')
    print(' '+ tabuleiro[2][0]+' '+tabuleiro[2][1]+' '+tabuleiro[2][2]+' ')
    print('      ')
    
def verificaVencedor(nome, simboloIndex):
    vencedor = 0
    soma = 0
    cont = 0
    soma_diagonal = 0
    soma_diagonal_sec = 0
    for x in range(0,3):
        for y in range(0,3):
            valor = 0
            if tabuleiro[x][y] == simbolos[simboloIndex]:
                valor = 1
            elif tabukeiro[x][y] == sombolos[not simboloIndex]:
                valor = -1
            else:
                valor = 999
                cont = cont + 1
                soma = soma + valor
                if (x == y):
                    soma_diagonal = valor + soma_diagonal
                if (x + y == 2):
                    soma_diagonal_sec = valor + soma_diagonal_sec
                    
        if (soma in [1,-1] and cont == 9):
            vencedor = 999
        if (soma_diagonal in [3,-3]):
            vencedor = soma_diagonal
        if (soma_diagonal_sec in [3,-3]):
            vencedor = soma_diagonal_sec
        soma_linha = 0
        for x in range(0,3):
            for y in range(0,3):
                valor = 0
                if tabuleiro[x][y] == simbolos[simboloIndex]:
                valor = 1
            elif tabukeiro[x][y] == sombolos[not simboloIndex]:
                valor = -1
            else:
                valor = 999
            soma_linha = soma_linha + valor
        if (soma_linha in [3,-3]):
            vencedor = soma_linha
            break
        else:
            soma_linha = 0
    soma_coluna = 0
    for y range(0, 3):
            for x in range(0,3):
                valor = 0
                if tabuleiro[x][y] == simbolos[simboloIndex]:
                valor = 1
            elif tabukeiro[x][y] == sombolos[not simboloIndex]:
                valor = -1
            else:
                valor = 999
                soma_coluna = soma_coluna + valor
        if (soma_coluna in [3,-3]):
            vencedor = soma_coluna
            break
        else:
            soma_coluna = 0
    return vencedor
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
            