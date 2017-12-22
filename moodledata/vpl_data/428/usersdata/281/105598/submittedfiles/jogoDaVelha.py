# -*- coding: utf-8 -*-
import random
from jogoDaVelha_BIB import*

def sorteioPrimeiraJogada():
    # Escolhe quem joga primeiro
    if random.randint (0,1) == 0:
        return 'computer'
    else:
        return nomeJogador


def mostrarTabuleiro(board):
    # Replicar a tabela com resultados
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def validaJogada(board, move):
    # Retorna true se o movimento feito é válido
    return board[move] == ' '

def jogadaHumana(board):
    # Captura o movimento do player
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not validaJogada(board, int(move)):
        print('Qual o seu próximo movimento, ' + nomeJogador + '? (linha coluna)')
        move = input()
        if move == '0 0':
            move = '7'
        elif move == '0 1':
            move = '8'
        elif move == '0 2':
            move = '9'
        elif move == '1 0':
            move = '4'
        elif move == '1 1':
            move = '5'
        elif move == '1 2':
            move = '6'
        elif move == '2 0':
            move = '1'
        elif move == '2 1':
            move = '2'
        elif move == '2 2':
            move = '3'
    return int(move)

def movimentoRandomicoComputador(board, movesList):
    # Retorna um movimento válido randomico
    # Retorna "none" se não houver movimento válido
    possibleMoves = []
    for i in movesList:
        if validaJogada(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def jogadaComputador(board, computerLetter):
    # Retorna movimento do computer
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    ### IA ###
    # Checa se pode ganhar no proximo movimento
    for i in range(1, 10):
        copy = mostrarTabuleiro(board)
        if validaJogada(copy, i):
            fazerMovimento(copy, computerLetter, i)
            if verificaVencedor(copy, computerLetter):
                return i

    # Checa se o player pode ganhar no próximo movimento e bloqueia ele
    for i in range(1, 10):
        copy = mostrarTabuleiro(board)
        if validaJogada(copy, i):
            fazerMovimento(copy, playerLetter, i)
            if verificaVencedor(copy, playerLetter):
                return i

    # Tenta em uma das extremidades
    move = movimentoRandomicoComputador(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Tenta no centro
    if validaJogada(board, 5):
        return 5

    # Tenta em um dos lados
    return movimentoRandomicoComputador(board, [2, 4, 6, 8])

def tabelaCompleta(board):
    # Retorna true se todos os espaços tiverem sido preenchidos
    for i in range(1, 10):
        if validaJogada(board, i):
            return False
    return True


print('Bem vindo ao Jogo da Velha da equipe C-ESSI!')
print('Quem está jogando: ')
nomeJogador = input()

while True:
    # Reseta a tabela
    theBoard = [' '] * 10
    playerLetter, computerLetter = solicitaSimboloDoHumano()
    turn = sorteioPrimeiraJogada()
    print('O ' + turn + ' joga primeiro.')
        gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Turno do player.
            desenhaTabela(theBoard)
            move = jogadaHumana(theBoard)
            fazerMovimento(theBoard, playerLetter, move)

            if verificaVencedor(theBoard, playerLetter):
                desenhaTabela(theBoard)            
                print(nome + ' ganhou. Obrigado.')
                gameIsPlaying = False
            else:
                if tabelaCompleta(theBoard):
                    desenhaTabela(theBoard)
                    print('Deu velha,EMPATE! ')
                    break
                else:
                    turn = 'computer'

        else:
            # Turno do computer.
            move = jogadaComputador(theBoard, computerLetter)
            fazerMovimento(theBoard, computerLetter, move)

            if verificaVencedor(theBoard, computerLetter):
                desenhaTabela(theBoard)
                print('o PC venceu, que pena, não foi dessa vez')
                gameIsPlaying = False
            else:
                if tabelaCompleta(theBoard):
                    desenhaTabela(theBoard)
                    print('EMPATE! DEU VELHA')
                    break
                else:
                    turn = 'player'

    if not jogarNovamente():
        break


    
    




       
    


    



    
        
        
   
