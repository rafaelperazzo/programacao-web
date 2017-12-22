# -*- coding: utf-8 -*-
import random
from jogoDaVelha_BIB import*

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

    
    




       
    


    



    
        
        
   
