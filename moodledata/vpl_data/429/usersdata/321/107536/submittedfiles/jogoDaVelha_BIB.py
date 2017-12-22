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
     while True:
        c= int(input('Qual a sua jogada, %s? ' % nome))
        x = c // 10
        y = c % 10
        if validaJogada(nome,tabuleiro,x,y,b):
            tabuleiro[x][y]= ' '+b+' '
            return True
    #else:
        #return False

def JogadaComputador(computador):
    while True:
        linha= random.randint(0,2)
        coluna= random.randint(0,2)
        if tabuleiro[linha][coluna]=='   ':
            tabuleiro[linha][coluna] = computador
            return True

def mostrarTabuleiro() :
    print('           ')
    print(tabuleiro[0][0]+'|'+tabuleiro[0][1]+'|'+tabuleiro[0][2])
    print('           ')
    print(tabuleiro[1][0]+'|'+tabuleiro[1][1]+'|'+tabuleiro[1][2])
    print('           ')
    print(tabuleiro[2][0]+'|'+tabuleiro[2][1]+'|'+tabuleiro[2][2])
    print('           ')
    
def validaJogada(nome,tabuleiro,l,c,s) :
    jogadapossivel = False 
    if not tabuleiro[l][c]=='   ':
        if nome!='':
            print('OPS!!! Essa jogada não está disponível. Tente novamente!')
            return False
    else:
        return True

'''
def verificaVencedor(s,tabuleiro,nome):
    if (tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == s or 
        tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == s or 
        tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == s or 
        tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == s or
        tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == s or
        tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == s or
        tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == s or 
        tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == s ):
            w= tabuleiro [0][0]
            if w==s:
                print('Vencedor: %s' %nome)
                return True
            else:
                print('Vencedor: Computador')
                return True
    else:
        cont=0
        for i in range(0,len(tabuleiro)):
            for j in range(0,len(tabuleiro)):
                if tabuleiro[i][j]!='   ':
                    cont += 1
        if cont==9:
            print ('Deu Velha')
            return True
        else:
            return False
'''                       


def verificaVencedor(s,tabuleiro,nome):
    if (tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2]) and tabuleiro[0][0]!='   ' :
        w= tabuleiro[0][0]
        if w==s:
            print('Vencedor: %s %w' %nome)
            return True
        else:
            print('Vencedor: %s %w Computador')
            return True
    elif (tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2]) and tabuleiro[1][0]!='   ' :
        w= tabuleiro[1][0]
        if w==s:
            print('Vencedor: %s %w' %nome)
            return True
        else:
            print('Vencedor: %s %w Computador')
            return True
    elif (tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2]) and tabuleiro[2][0]!='   ' :
        w= tabuleiro[2][0]
        if w==s:
            print('Vencedor: %s %w' %nome)
            return True
        else:
            print('Vencedor: %s %w Computador')
            return True
    elif (tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]) and tabuleiro[0][0]!='   ' :
        w= tabuleiro[0][0]
        if w==s:
            print('Vencedor: %s %w' %nome)
            return True
        else:
            print('Vencedor: %s %w Computador')
            return True
    elif (tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]) and tabuleiro[0][1]!='   ' :
        w= tabuleiro[0][1]
        if w==s:
            print('Vencedor: %s %w' %nome)
            return True
        else:
            print('Vencedor: %s %w Computador')
            return True
    elif (tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]) and tabuleiro[0][2]!='   ' :
        w= tabuleiro[0][2]
        if w==s:
            print('Vencedor: %s %w' %nome)
            return True
        else:
            print('Vencedor: %s %w Computador')
            return True
    elif (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]) and tabuleiro[0][0]!='   ' :
        w= tabuleiro[0][0]
        if w==s:
            print('Vencedor: %s %w' %nome)
            return True
        else:
            print('Vencedor: %s %w Computador')
            return True
    elif (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]) and tabuleiro[0][2]!='   ' :
        w= tabuleiro[0][2]
        if w==s:
            print('Vencedor: %s %w' %nome)
            return True
        else:
            print('Vencedor: %s %w Computador')
            return True
    else:
        cont=0
        for i in range(0,3,1):
            for j in range(0,3,1):
                if tabuleiro[i][j]!='   ':
                    cont += 1
        if cont==9:
            print ('Deu Velha')
            return True
        else:
            return False

def jogueNovamente():
    print('Você quer jogar de novo? (sim ou não)')
    return input().lower().startswith('y')
    
  #Olhar o erro
  
'''
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
