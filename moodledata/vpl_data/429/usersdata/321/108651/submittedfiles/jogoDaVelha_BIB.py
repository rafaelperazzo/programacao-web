# # -*- coding: utf-8 -*-

# # COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
# import random

# tabuleiro = [
#     ['   ','   ','   '],
#     ['   ','   ','   '],
#     ['   ','   ','   ']]

# def nome():
#     nome = str(input('Qual seu nome? \n'))
#     return nome
    
# def solicitaSimboloDoHumano():
#     s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) \n'))
#     while s != 'X' and s != 'O':
#         print('Insira um símbolo válido.')
#         s = str(input('Qual símbolo você deseja utilizar no jogo? (X ou O) '))
#     return s

# def sorteioPrimeiraJogada(nome):
#     j1 = nome
#     j2 = 'Computador'
#     sort = random.randint(0,1)
#     if sort == 1:
#         print ('Vencedor do sorteio para início do jogo: %s' % j1)
#     if sort == 0:
#         print ('Vencedor do sorteio para início do jogo: %s' % j2)
#     return sort
    
# def JogadaHumana(nome,b):
#      while True:
#         c= int(input('Qual a sua jogada, %s? ' % nome))
#         x = c // 10
#         y = c % 10
#         if validaJogada(nome,tabuleiro,x,y,b):
#             tabuleiro[x][y]= ' '+b+' '
#             return True
#     #else:
#         #return False

# def JogadaComputador(computador):
#     while True:
#         linha= random.randint(0,2)
#         coluna= random.randint(0,2)
#         if tabuleiro[linha][coluna]=='   ':
#             tabuleiro[linha][coluna] = computador
#             return True

# def mostrarTabuleiro() :
#     print('           ')
#     print(tabuleiro[0][0]+'|'+tabuleiro[0][1]+'|'+tabuleiro[0][2])
#     print('           ')
#     print(tabuleiro[1][0]+'|'+tabuleiro[1][1]+'|'+tabuleiro[1][2])
#     print('           ')
#     print(tabuleiro[2][0]+'|'+tabuleiro[2][1]+'|'+tabuleiro[2][2])
#     print('           ')
    
# def validaJogada(nome,tabuleiro,l,c,s) :
#     jogadapossivel = False 
#     if not tabuleiro[l][c]=='   ':
#         if nome!='':
#             print('OPS!!! Essa jogada não está disponível. Tente novamente!')
#             return False
#     else:
#         return True

# '''
# def verificaVencedor(s,tabuleiro,nome):
#     if (tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == s or 
#         tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == s or 
#         tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == s or 
#         tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == s or
#         tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == s or
#         tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == s or
#         tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == s or 
#         tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == s ):
#             w= tabuleiro [0][0]
#             if w==s:
#                 print('Vencedor: %s' %nome)
#                 return True
#             else:
#                 print('Vencedor: Computador')
#                 return True
#     else:
#         cont=0
#         for i in range(0,len(tabuleiro)):
#             for j in range(0,len(tabuleiro)):
#                 if tabuleiro[i][j]!='   ':
#                     cont += 1
#         if cont==9:
#             print ('Deu Velha')
#             return True
#         else:
#             return False
# '''                       


# def verificaVencedor(s,tabuleiro,nome):
#     if (tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2]) and tabuleiro[0][0]!='   ' :
#         w= tabuleiro[0][0]
#         if w.strip()==s:
#             print('Vencedor: %s' %nome)
#             return True
#         else:
#             print('Vencedor: Computador')
#             return True
#     elif (tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2]) and tabuleiro[1][0]!='   ' :
#         w= tabuleiro[1][0]
#         if w.strip()==s:
#             print('Vencedor: %s' %nome)
#             return True
#         else:
#             print('Vencedor: Computador')
#             return True
#     elif (tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2]) and tabuleiro[2][0]!='   ' :
#         w= tabuleiro[2][0]
#         if w.strip()==s:
#             print('Vencedor: %s' %nome)
#             return True
#         else:
#             print('Vencedor: Computador')
#             return True
#     elif (tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]) and tabuleiro[0][0]!='   ' :
#         w= tabuleiro[0][0]
#         if w.strip()==s:
#             print('Vencedor: %s' %nome)
#             return True
#         else:
#             print('Vencedor: Computador')
#             return True
#     elif (tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]) and tabuleiro[0][1]!='   ' :
#         w= tabuleiro[0][1]
#         if w.strip()==s:
#             print('Vencedor: %s' %nome)
#             return True
#         else:
#             print('Vencedor: Computador')
#             return True
#     elif (tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]) and tabuleiro[0][2]!='   ' :
#         w= tabuleiro[0][2]
#         if w.strip()==s:
#             print('Vencedor: %s' %nome)
#             return True
#         else:
#             print('Vencedor: Computador')
#             return True
#     elif (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]) and tabuleiro[0][0]!='   ' :
#         w= tabuleiro[0][0]
#         if w.strip()==s:
#             print('Vencedor: %s' %nome)
#             return True
#         else:
#             print('Vencedor: Computador')
#             return True
#     elif (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]) and tabuleiro[0][2]!='   ' :
#         w= tabuleiro[0][2]
#         if w.strip()==s:
#             print('Vencedor: %s' %nome)
#             return True
#         else:
#             print('Vencedor: Computador')
#             return True
#     else:
#         cont=0
#         for i in range(0,3,1):
#             for j in range(0,3,1):
#                 if tabuleiro[i][j]!='   ':
#                     cont += 1
#         if cont==9:
#             print ('Deu Velha')
#             return True
#         else:
#             return False

# def jogueNovamente():
#     print('Você quer jogar de novo? (sim ou não)')
#     return input().lower().startswith('y')
    
#   #Olhar o erro
  
# '''
# def verifica(m,situacao):
#     flag=False
#     if (m[0][0]==m[0][1]==m[0][2]=='X'):
#         print 'Jogador 1 ganhou'
#         situacao=True
#     elif (m[1][0]==m[1][1]==m[1][2]=='X'):
#         print 'Jogador 1 ganhou'
#         situacao=True
#     elif (m[2][0]==m[2][1]==m[2][2]=='X'):
#         print 'Jogador 1 ganhou'
#         situacao=True
#     elif (m[0][0]==m[1][0]==m[2][0]=='X'):
#         print 'Jogador 1 ganhou'
#         situacao=True
#     elif (m[0][1]==m[1][1]==m[2][1]=='X'):
#         print 'Jogador 1 ganhou'
#         situacao=True
#     elif (m[0][2]==m[1][2]==m[2][2]=='X'):
#         print 'Jogador 1 ganhou'
#         situacao=True
#     elif (m[0][0]==m[1][1]==m[2][2]=='X'):
#         print 'Jogador 1 ganhou'
#         situacao=True
#     elif (m[0][2]==m[1][1]==m[2][0]=='X'):
#         print 'Jogador 1 ganhou'
#         situacao=True
#     elif (m[0][0]==m[0][1]==m[0][2]=='0'):
#         print 'Jogador 1 ganhou'
#         situacao=True
#     elif (m[1][0]==m[1][1]==m[1][2]=='0'):
#         print 'Jogador 1 ganhou'
#         situacao=True
#     elif (m[2][0]==m[2][1]==m[2][2]=='0'):
#         print 'Jogador 1 ganhou'
#         situacao=True
#     elif (m[0][0]==m[1][0]==m[2][0]=='0'):
#         print 'Jogador 1 ganhou'
#         situacao=True
#     elif (m[0][1]==m[1][1]==m[2][1]=='0'):
#         print 'Jogador 1 ganhou'
#         situacao=True
#     elif (m[0][2]==m[1][2]==m[2][2]=='0'):
#         print 'Jogador 1 ganhou'
#         situacao=True
#     elif (m[0][0]==m[1][1]==m[2][2]=='0'):
#         print 'Jogador 1 ganhou'
#         situacao=True
#     elif (m[0][2]==m[1][1]==m[2][0]=='0'):
#         print ('Jogador 1 ganhou')
#         situacao=True
#     else:
#         for i in matriz:
#             for j in i:
#                 if j=='   ':
#                     flag=True
#                     if flag==False:
#                         print ('Deu Velha')
#                         situacao=True
#     return situacao
# '''    

#---------------------------------------------------------
# por Iara
#---------------------------------------------------------

# -*- coding: utf-8 -*-
import random

# apenas para python 2.7
#input = eval('raw_input')

#tabuleiro
tabuleiro = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#simbolos
simbolos = ['X', 'O']
#jogadas
jogadasPossiveis = ['0', '1', '2']


# solicita ao usuário o símbolo que ele deseja 
# utilizar na partida e garante que ele informou 
# um símbolo válido (X ou O);
def solicitaSimboloDoHumano(): 
    s = ''
    while True:
        s = input('\nQual símbolo você deseja utilizar no jogo? ')
        if not(s in simbolos):
            print('\nPor favor, selecione um símbolo válido: X ou O')
            continue
        if s == simbolos[0]:
            return 0
        else:
            return 1

# realiza um sorteio totalmente aleatório para 
# definir quem começa o jogo (humano ou computador);
def sorteioPrimeiraJogada(nome): 
    r = random.randint(0,1)
    if r == 0:
        print ('\nVencedor do sorteio para início do jogo: %s'  % Computador')
    else:
        print ('\nVencedor do sorteio para início do jogo: %s' % nome)
    return r

# verifica se o jogador inseriu ou realizou uma jogada válida;
def validaJogada(xy):
    # é válido se tiver dois valores
    if len(xy) != 2:
        return False
    # verificar se x e y é do tipo inteiro
    if not xy[0] in jogadasPossiveis:
        return False
    if not xy[1] in jogadasPossiveis:
        return False
    #jogada separada
    x = int(xy[0])
    y = int(xy[1])
    # se houver local disponível no tabuleiro
    if not tabuleiro[x][y] == ' ':
        return False
    #se tudo for válido retorna os valores
    return True

# recebe uma jogada válida do usuário;
def jogadaHumana(nome, simboloIndex):
     while True:
        jogada = input('\nQual a sua jogada, %s? ' % nome)
        # separa em duas entradas
        xy = jogada.split(' ')
        if validaJogada(xy):
            x = int(xy[0])
            y = int(xy[1])
            tabuleiro[x][y] = simbolos[simboloIndex]
            break
        else:
            print('\nOPS!!! Essa jogada não está disponível. Tente novamente!')

# realiza uma jogada válida pelo computador;
def jogadaComputador(simboloIndex):
    while True:
        x = random.randint(0,2)
        y = random.randint(0,2)
        if tabuleiro[x][y] == ' ':
            tabuleiro[x][y] = simbolos[not simboloIndex]
            break

# exibe o tabuleiro atualizado na tela.
def mostraTabuleiro():
    print('           ')
    print(' ' + tabuleiro[0][0]+' | '+tabuleiro[0][1]+' | '+tabuleiro[0][2] + ' ')
    print('           ')
    print(' ' + tabuleiro[1][0]+' | '+tabuleiro[1][1]+' | '+tabuleiro[1][2] + ' ')
    print('           ')
    print(' ' + tabuleiro[2][0]+' | '+tabuleiro[2][1]+' | '+tabuleiro[2][2] + ' ')
    print('           ')

# verifica se há vencedor ou empate e, caso positivo, 
# exibe “Vencedor: Computador” (sem as aspas) ou “Vencedor: nome” 
# (nome é o valor do nome ou apelido do jogador humano 
# informado no começo, sem as aspas) ou “Deu Velha!” (empate!, sem as aspas).
def verificaVencedor(nome, simboloIndex): 
    # vencedor
    vencedor = 0
    # percorrer toda matrix
    soma = 0
    cont = 0
    soma_diagonal = 0
    soma_diagonal_sec = 0
    for x in range(0, 3):
        for y in range(0, 3):
            # valor do tabuleiro
            valor = 0
            # converter valor simbolos[simboloIndex] em 1 e O em -1
            if tabuleiro[x][y] == simbolos[simboloIndex]:
                valor = 1
            elif tabuleiro[x][y] == simbolos[not simboloIndex]:
                valor = -1
            else:
                valor = 999
            #
            cont = cont + 1
            soma = soma + valor
            # somar diagonais (principal e secundária)
            if (x == y):
                soma_diagonal = valor + soma_diagonal
            if (x + y == 2):
                soma_diagonal_sec = valor + soma_diagonal_sec

    #se for 3 ou -3 houve vencedor na diagonal
    if (soma in [1, -1] and cont == 9):
        vencedor = 999
    if (soma_diagonal in [3, -3]):
        vencedor = soma_diagonal
    if (soma_diagonal_sec in [3, -3]):
        vencedor = soma_diagonal_sec
    # percorrer todas as colunas
    soma_linha = 0
    for x in range(0, 3):
        for y in range(0, 3):
            # valor do tabuleiro
            valor = 0
            # converter valor X em 1 e O em -1
            if tabuleiro[x][y] == simbolos[simboloIndex]:
                valor = 1
            elif tabuleiro[x][y] == simbolos[not simboloIndex]:
                valor = -1
            else:
                valor = 999
            # somar colunas
            soma_linha = soma_linha + valor
        if (soma_linha in [3, -3]):
            vencedor = soma_linha
            break
        else:
            soma_coluna = 0
    # percorrer todas as linhas
    soma_coluna = 0
    for y in range(0, 3):
        for x in range(0, 3):
            # valor do tabuleiro
            valor = 0
            # converter valor X em 1 e O em -1
            if tabuleiro[x][y] == 'X':
                valor = 1
            elif tabuleiro[x][y] == 'O':
                valor = -1
            else:
                valor = 0
            # somar colunas
            soma_coluna = soma_coluna + valor
        if (soma_coluna in [3, -3]):
            vencedor = soma_coluna
            break
        else:
            soma_linha = 0
    # se não encontrar vencedor
    if (vencedor == 3):
        print ('Vencedor: %s '% nome)
        return True
    elif vencedor == -3:
        print ('Vencedor: Computador')
        return True
    elif vencedor == 999:
        print ('Deu velha')
        return True
    # não houve vencedor
    return False
