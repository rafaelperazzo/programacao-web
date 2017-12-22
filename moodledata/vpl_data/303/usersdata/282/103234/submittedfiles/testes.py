# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import random

def drawBoard(board):
    # Desenha a tabela

    # "board" é uma lista de 10 strings representando uma tabela (ignorando o indice [0])
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    # Escolhe a letra
    
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Você quer ser X ou O?')
        letter = input().upper()

    # Define a letra do computador
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Escolhe quem joga primeiro
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('Quer jogar de novo? (s ou n)')
    return input().lower().startswith('s')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # topo
    (bo[4] == le and bo[5] == le and bo[6] == le) or # meio
    (bo[1] == le and bo[2] == le and bo[3] == le) or # baixo
    (bo[7] == le and bo[4] == le and bo[1] == le) or # vertical esquerdo
    (bo[8] == le and bo[5] == le and bo[2] == le) or # vertical meio
    (bo[9] == le and bo[6] == le and bo[3] == le) or # vertical direito
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # Replicar a tabela com resultados
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # Retorna true se o movimento feito é válido
    return board[move] == ' '

def getPlayerMove(board):
    # Captura o movimento do player
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Qual o seu próximo movimento? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Retorna um movimento válido randomico
    # Retorna "none" se não houver movimento válido
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Retorna movimento do computer
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    ### IA ###
    # Checa se pode ganhar no proximo movimento
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Checa se o player pode ganhar no próximo movimento e bloqueia ele
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Tenta em uma das extremidades
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Tenta no centro
    if isSpaceFree(board, 5):
        return 5

    # Tenta em um dos lados
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Retorna true se todos os espaços tiverem sido preenchidos
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Bem vindo ao famigerado Jogo da Velha!')

while True:
    # Reseta a tabela
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('O ' + turn + ' joga primeiro.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Turno do player.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                #print('Hooray! You have won the game!')
                print('Agradecimentos ao incrívelmente magnífico: Gabriel Ferreira. Obrigado. Imposto é roubo e mulher é merda.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('EMPATE! Fã do Goku nem é gente')
                    break
                else:
                    turn = 'computer'

        else:
            # Turno do computer.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Uma IA venceu você, que desprezível...')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('EMPATE! Fã do Goku nem é gente')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break