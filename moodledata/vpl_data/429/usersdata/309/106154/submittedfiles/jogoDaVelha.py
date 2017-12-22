# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *
import os


jn='s'
while jn=='s' or jn == 'S':
    os.system('clear')
    print('Bem vindo ao Jogo da Velha! Grupo C [Ana Larissa, Anderson Zhong Fan, Nicolas]')
    
    #definindo o tabuleiro 
    tabuleiro=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    
    #nome do jogador
    nome=input('\nQual seu nome(ou apelido)? ')
    #chamando a função da soli. do simbolo humano  
    simbH=solicitaSimboloDoHumano()
    
    # definição do simbolo da máquina
    if simbH=="X":
            simbM="O"
    else:
        simbM="X"
        
    #sorteio da 1ª jogada, e definição de quem fará a próxima jogada    
    prop=sorteioPrimeiraJogada (simbM, simbH, tabuleiro, nome)
    
    
    #Condição para definir as jogadas posteriores 
    if prop==1:
        #função para pedir a jogada humana
        tabuleiro=jogadaHumana(nome, simbH, tabuleiro)
        tabuleiro=jogadaComputador(tabuleiro, simbM)
        mostraTabuleiro(tabuleiro)
        tabuleiro=jogadaHumana(nome, simbH, tabuleiro)
        
       
        while True:
            tabuleiro=jogadaComputador(tabuleiro, simbM)
            x=VerificaVencedor(tabuleiro, simbH, nome, simbM)
          
            if x%2==0:
                mostraTabuleiro(tabuleiro)
                if x==2:
                    print("\n Vencedor: %s" %nome)
                elif x==4:
                    print("\n Vencedor: Computador")
                else:
                    print ("\n Deu velha!")
                break
            
            tabuleiro=jogadaHumana(nome, simbH, tabuleiro)
            x=VerificaVencedor(tabuleiro, simbH, nome, simbM)
            if x%2==0:
                mostraTabuleiro(tabuleiro)
                if x==2:
                    print("\n Vencedor: %s" %nome)
                elif x==4:
                    print("\n Vencedor: Computador")
                else:
                    print ("\n Deu velha!")
                break
            mostraTabuleiro(tabuleiro)
    else:
        tabuleiro=jogadaHumana(nome, simbH, tabuleiro)
        tabuleiro=jogadaComputador(tabuleiro, simbM)
        mostraTabuleiro(tabuleiro)
        tabuleiro=jogadaHumana(nome, simbH, tabuleiro)
        tabuleiro=jogadaComputador(tabuleiro, simbM)
        mostraTabuleiro(tabuleiro)
        
        while True:
            tabuleiro=jogadaHumana(nome, simbH, tabuleiro) # começa a verificação
            x=VerificaVencedor(tabuleiro, simbH, nome, simbM)
            #tabuleiro=jogadaComputador(tabuleiro, simbM)
            #mostraTabuleiro(tabuleiro)
            if x%2==0:
                mostraTabuleiro(tabuleiro)
                if x==2:
                    print("\n Vencedor: %s" %nome)
                elif x==4:
                    print("\n Vencedor: Computador")
                else:
                    print ("\n Deu velha!")
                break
            tabuleiro=jogadaComputador(tabuleiro, simbM)
            x=VerificaVencedor(tabuleiro, simbH, nome, simbM)
            if x%2==0:
                mostraTabuleiro(tabuleiro)
                if x==2:
                    print("\n Vencedor: %s" %nome)
                elif x==4:
                    print("\n Vencedor: Computador")
                else:
                    print ("\n Deu velha!")
                break
            mostraTabuleiro(tabuleiro)
            
            
    jn=str(input('\n\n Deseja jogar novamente ?(s ou n)'))
    while jn!='n' and jn!='N' and jn!='s' and jn!='S':
        print ('\nNão reconheço essa opção...')
        jn=str(input('\nDeseja jogar novamente ?(s ou n)'))
    if jn=='n' or jn=='N':
        print('\n\nVocê jogou bem... Até logo !')
    