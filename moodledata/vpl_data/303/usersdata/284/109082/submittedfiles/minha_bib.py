
import random

def solicitaSimboloDoHumano():
    letra = 0
    while not (letra == 'O' or letra == 'X'):
        print('Qual símbolo você deseja utilizar no jogo? (X ou O) ')
        letra = input().upper()

    if letra == 'X':
        return ['X','O']
    else:
        return ['O','X']

def sorteioPrimeiraJogada():
    if random.randrange(2) == 1:
        return 'Computador'
    else:
        return 'Jogador'

def jogadaHumana(tabuleiro,nome):
    movimento = 0 
    while movimento not in '1 2 3 4 5 6 7 8 9'.split() or not vazio(tabuleiro, int(movimento)):
        print('Qual a sua jogada, {}?'.format(nome))
        movimento = input()
        if movimento == '00':
            movimento= '7'
        elif movimento == '01':
            movimento= '8'
        elif movimento == '02':
            movimento= '9'
        elif movimento == '10':
            movimento= '4'
        elif movimento == '11':
            movimento= '5'
        elif movimento == '12':
            movimento= '6'
        elif movimento == '20':
            movimento= '1'
        elif movimento == '21':
            movimento= '2' 
        elif movimento == '22':
            movimento= '3'
    return int(movimento)

def jogadaComputador(tabuleiro, letraComputador):
    if letraComputador == 'X':
        letraJogador = 'O'
    else:
        letraJogador = 'X'
    for i in range(1,10):
        mostra = mostraTabuleiro(tabuleiro)
        if vazio(mostra, i):
            movimentacao(mostra, letraComputador, i)
            if verificaVencedor(mostra, letraComputador):
                return i

    for i in range(1, 10):
        mostra = mostraTabuleiro(tabuleiro)
        if vazio(mostra, i):
            movimentacao(mostra, letraJogador, i)
            if verificaVencedor(mostra, letraJogador):
                return i

    movimento = movAleatoria(tabuleiro, [1, 3, 7, 9])
    if movimento != None:
        return movimento

    if vazio(tabuleiro, 5):
        return 5

    return movAleatoria(tabuleiro, [2, 4, 6, 8])

def mostraTabuleiro(tabuleiro):
    novoTabuleiro = []

    for i in tabuleiro:
        novoTabuleiro.append(i)

    return novoTabuleiro

def verificaVencedor(tabuleiro, letra):
    return ((tabuleiro[7] == letra and tabuleiro[8] == letra and tabuleiro[9] == letra) or
            (tabuleiro[4] == letra and tabuleiro[5] == letra and tabuleiro[6] == letra) or
            (tabuleiro[1] == letra and tabuleiro[2] == letra and tabuleiro[3] == letra) or
            (tabuleiro[7] == letra and tabuleiro[4] == letra and tabuleiro[1] == letra) or
            (tabuleiro[8] == letra and tabuleiro[5] == letra and tabuleiro[2] == letra) or
            (tabuleiro[9] == letra and tabuleiro[6] == letra and tabuleiro[3] == letra) or
            (tabuleiro[7] == letra and tabuleiro[5] == letra and tabuleiro[3] == letra) or
            (tabuleiro[9] == letra and tabuleiro[5] == letra and tabuleiro[1] == letra))

def vazio(tabuleiro, movimento):
    return tabuleiro[movimento] == ' '

def desenhaTabuleiro(tabuleiro):
    print(' ' + tabuleiro[7] + ' | ' + tabuleiro[8] + ' | ' + tabuleiro[9])
    print(' ' + tabuleiro[4] + ' | ' + tabuleiro[5] + ' | ' + tabuleiro[6])
    print(' ' + tabuleiro[1] + ' | ' + tabuleiro[2] + ' | ' + tabuleiro[3])

def jogarNovamente():
    print('Você deseja jogar novamente?(sim ou não)')
    return input().startswith('sim')

def movimentacao(tabuleiro, letra, movimento):
    tabuleiro[movimento] = letra

def movAleatoria(tabuleiro, movimentosList):
    movPossiveis = []
    for i in movimentosList:
        if vazio(tabuleiro, i):
            movPossiveis.append(i)

    if len(movPossiveis) != 0:
        return random.choice(movPossiveis)
    else:
        return None

def completo(tabuleiro):
    for i in range(1, 10):
        if vazio(tabuleiro, i):
            return False
    return True
    