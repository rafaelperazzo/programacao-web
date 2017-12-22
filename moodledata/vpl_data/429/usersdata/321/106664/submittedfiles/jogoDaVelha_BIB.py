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
    tabuleiro[x][y]= ' '+b+' '
    return True


def jogadaComputador(computador):
    linha = random.randint(0,2)
    coluna= random.randint(0,2)
    tabuleiro[linha][coluna] = computador
    return True
   
def mostrarTabuleiro() : 
    print(tabuleiro[0][0]+'|'+tabuleiro[0][1]+'|'+tabuleiro[0][2])
    print(tabuleiro[1][0]+'|'+tabuleiro[1][1]+'|'+tabuleiro[1][2])
    print(tabuleiro[2][0]+'|'+tabuleiro[2][1]+'|'+tabuleiro[2][2])
    
def validaJogada(jogadaHumana,jogadaComputador,tabuleiro,s) :
    jogadapossivel = False 
    if jogadaHumana()!='   ' or jogadaComputador !='   ':
        print('OPS!!! Essa jogada não está disponível. Tente novamente!')
        return False
    else:
       jogadaComputador(s)
       return True
    
def verificaVencedor(s,tabuleiro,nome):
    if False:
        if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] and not bool(tabuleiro[0][0]) :
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
        '''print('Deu Velha!')
        return False'''
        for i in tabuleiro:
            for j in i:
                if j=='   ':
                    flag=True
                    if flag==False:
                        print ('Deu Velha')
                        situacao=True

def jogueNovamente():
    print('Você quer jogar de novo? (sim ou não)')
    return input().lower().startswith('y')
  #Olhar o erro
  
'''
 def determineVictory(board):
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
    return False

def determineAvailableMoves(board) :
    rows = ['top','mid','low']
    cols = ['L','M','R']
    hasMoves = False
    # verifica se posicão escolhida é válida
    for r in rows :
        for c in cols :
            key = str(r) + '-' + str(c)
            if not bool(board[key]) :
                return True
    return hasMoves

def verifica(m,situacao):
    flag=False
    if (m[0][0]==m[0][1]==m[0][2]=='X'):
        print 'Jogador 1 ganhou'
        situacao=True
    elif (m[1][0]==m[1][1]==m[1][2]=='X'):
        print 'Jogador 1 ganhou'
        situacao=True
    elif (m[2][0]==m[2][1]==m[2][2]=='X'):
        print 'Jogador 1 ganhou'
        situacao=True
    elif (m[0][0]==m[1][0]==m[2][0]=='X'):
        print 'Jogador 1 ganhou'
        situacao=True
    elif (m[0][1]==m[1][1]==m[2][1]=='X'):
        print 'Jogador 1 ganhou'
        situacao=True
    elif (m[0][2]==m[1][2]==m[2][2]=='X'):
        print 'Jogador 1 ganhou'
        situacao=True
    elif (m[0][0]==m[1][1]==m[2][2]=='X'):
        print 'Jogador 1 ganhou'
        situacao=True
    elif (m[0][2]==m[1][1]==m[2][0]=='X'):
        print 'Jogador 1 ganhou'
        situacao=True
    elif (m[0][0]==m[0][1]==m[0][2]=='0'):
        print 'Jogador 1 ganhou'
        situacao=True
    elif (m[1][0]==m[1][1]==m[1][2]=='0'):
        print 'Jogador 1 ganhou'
        situacao=True
    elif (m[2][0]==m[2][1]==m[2][2]=='0'):
        print 'Jogador 1 ganhou'
        situacao=True
    elif (m[0][0]==m[1][0]==m[2][0]=='0'):
        print 'Jogador 1 ganhou'
        situacao=True
    elif (m[0][1]==m[1][1]==m[2][1]=='0'):
        print 'Jogador 1 ganhou'
        situacao=True
    elif (m[0][2]==m[1][2]==m[2][2]=='0'):
        print 'Jogador 1 ganhou'
        situacao=True
    elif (m[0][0]==m[1][1]==m[2][2]=='0'):
        print 'Jogador 1 ganhou'
        situacao=True
    elif (m[0][2]==m[1][1]==m[2][0]=='0'):
        print ('Jogador 1 ganhou')
        situacao=True
    else:
        for i in matriz:
            for j in i:
                if j=='   ':
                    flag=True
                    if flag==False:
                        print ('Deu Velha')
                        situacao=True
    return situacao
'''    
    

















