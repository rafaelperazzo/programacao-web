from jogoDaVelha_BIB import *

tabuleiro = [ [' ',' ',' '], [' ',' ',' '], [' ',' ',' '] ] #Tabuleiro vazio

grupo = 'H [Breendon, Gustavo, Roberto, Rafael]' #Nome dos integrantes do grupo
jogador = ['','']                                #Nome do jogador e simbolo
computador = ['Computador','']                   #Computador e simbolo



bemVindo(grupo)

jogador[0] = input('Qual o seu nome (ou apelido)? ')
jogador[1], computador[1] = solicitaSimboloDoHumano()

turno = sorteioPrimeiraJogada(jogador[0])
movimentos = 0
print('Vencedor do sorteio para início do jogo: {}' .format(turno))

while True :
    if turno == computador[0] :
        tabuleiro = jogadaComputador(tabuleiro, computador[1])
        mostraTabuleiro(tabuleiro)
        movimentos += 1
        acabou = verificaVencedor(tabuleiro, computador, movimentos)
        if acabou :
            break
        turno = jogador[0]
    else :
        while True :
            jogada = input('Qual a sua jogada, {}? ' .format(jogador[0]))
            jogadaValida = validaJogada(tabuleiro, jogada)
            if not jogadaValida :
                print('OPS!!! Essa jogada não está disponível. Tente novamente!')
            else :
                tabuleiro = jogadaHumana(tabuleiro, jogador[1], jogada)
                mostraTabuleiro(tabuleiro)
                movimentos += 1
                acabou = verificaVencedor(tabuleiro, jogador, movimentos)
                turno = computador[0]
                break
        if acabou :
            break
        
        
        

        
