# -*- coding: utf-8 -*-
import random
from jogoDaVelha_BIB import*

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

print('Bem vindo ao Jogo da Velha da equipe C-ESSI!')
nomeJogador=str(input('Quem está jogando: '))


while True:
    # Reseta a tabela
    theBoard = [' '] * 10
    playerLetter, computerLetter = solicitaSimboloDoHumano()
    turn = sorteioPrimeiraJogada()
    print('O ' + turn + ' joga primeiro.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'jogador' :
            # Turno do player.
            desenhaTabela(theBoard)
            move = jogadaHumana(theBoard)
            fazerMovimento(theBoard, playerLetter, move)

            if verificaVencedor(theBoard, playerLetter):
                desenhaTabela(theBoard)            
                print(nomeJogador + ' ganhou. Obrigado.')
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
                    turn = 'jogador'

    if not jogarNovamente():
        break

    
    




       
    


    



    
        
        
   
