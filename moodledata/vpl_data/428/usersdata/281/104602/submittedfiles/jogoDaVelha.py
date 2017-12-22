# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *
import random  
# COLOQUE SEU PROGRAMA A PARTIR DAQUI

print('Bem vindo ao Jogo da Velha da equipe C-ESSI!')
print('Quem está jogando: ')
nomeJogador = input()
print('\n-----------------------------------------------------------------')

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


    
    




       
    


    



    
        
        
   
