# -*- coding: utf-8 -*-
import random

# apenas para python 2.7
input = eval('raw_input')

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
        print '\nVencedor do sorteio para início do jogo: ', 'Computador'
    else:
        print '\nVencedor do sorteio para início do jogo: ', nome
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
            soma_linha = 0
    # percorrer todas as linhas
    soma_coluna = 0
    for y in range(0, 3):
        for x in range(0, 3):
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
            soma_coluna = soma_coluna + valor
        if (soma_coluna in [3, -3]):
            vencedor = soma_coluna
            break
        else:
            soma_coluna = 0
    #resultado
    return vencedor

# tabuleiro = [
#     ['X','O','O'],
#     ['X','O','X'],
#     [' ','O','X']]
# def testVerificaVencedor():
#     print verificaVencedor('Ari', 0)

# testVerificaVencedor()