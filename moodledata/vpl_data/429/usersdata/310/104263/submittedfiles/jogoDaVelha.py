# -*- coding: utf-8 -*-

from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
jgnov = 'S'
while jgnov == 'S' or jgnov =='s':
    print('Bem vindo ao JogoDaVelha do grupo D [Anderson Bezerra, Caio, Juan, Laura Nunes]')
    nome = input('\nQual o seu nome (ou apelido)? ')
    
    print('---------------------------------------------------')
    print('Olá, iniciaremos em 5 segundos, aguarde %s' %nome   )
    print('---------------------------------------------------')
    time.sleep(5)
    jogador = 2
    smbH = 0
    smbH = solicitaSimbolodoHumano(smbH)
    
    if smbH == ' X ':
        smbPC = ' O '
    else:
        smbPC = ' X '
    
    
    jogador = sorteioPrimeiraJogada(jogador, nome) #SorteioDaPrimeiraJogada
    
    
    tabuleiro = [                                                 
        ['   ','   ','   '],                #_/\/\/\/\/\/\/\/\_#                 
        ['   ','   ','   '],                #                  #
        ['   ','   ','   ']                 #    Tabuleiro     #
        ]                                   #                  #
                                            #_/\/\/\/\/\/\/\/\_#
    
    som = 0
    while True:
        if jogador == 1:
            while True:
                JogadaHumana(smbH,tabuleiro, nome)
                break
            
            if verificaVencedor(smbH, tabuleiro, som):  #Mostra que deu velha e printa'DeuVelha'.
                if verificaVencedor(smbH, tabuleiro, som) == 20:
                    mostraTabuleiro(tabuleiro)
                    print ('\nDeu Velha')
                    break
                else:
                    mostraTabuleiro(tabuleiro)
                    print('\nVencedor: %s'%nome) #Mostra o nome do jogador que venceu e retorna o tabuleiro.
                    break
            
            jogador = 0
        
        
        else:
            tabuleiro = JogadaComputador(smbPC,tabuleiro)
            
            if verificaVencedor(smbPC, tabuleiro, som):
                if verificaVencedor(smbPC, tabuleiro, som) == 20:
                    mostraTabuleiro(tabuleiro)
                    print ('\nDeu Velha') #Mostra que deu velha e printa'DeuVelha'
                    break
                else:
                    mostraTabuleiro(tabuleiro)
                    print ('\nVencedor: Computador') #Mostra que o Computador venceu e retorna o tabuleiro.
                    break
            
            
            jogador = 1
    print('\nCaso queira jogar novamente digite: S ou s')
    jgnov = input('\nQuer jogar novamente ? ')
    if jgnov == 'S' or jgnov == 's':
        os.system('clear')





