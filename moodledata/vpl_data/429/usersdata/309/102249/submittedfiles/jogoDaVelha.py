# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *


#definindo o tabuleiro 
tabuleiro=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

#nome do jogador
nome=input('Qual seu nome(ou apelido)? ')
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
    tabuleiro=jogada1computer(tabuleiro, simbM)
    mostraTabuleiro(tabuleiro)
    tabuleiro=jogadaHumana(nome, simbH, tabuleiro)
    tabuleiro=jogada1computer(tabuleiro, simbM)
    mostraTabuleiro(tabuleiro)
    x=VerificaVencedor(tabuleiro, simbH, nome)
   
    while x%2!=0:
        tabuleiro=jogadaHumana(nome, simbH, tabuleiro)
        x=VerificaVencedor(tabuleiro, simbH, nome)
        if x%==0:
            mostraTabuleiro(tabuleiro)
            if x==2:
            print("Vencedor: %s" %nome)
            elif x==4:
                print("Vencedor: ")
            break
        tabuleiro=jogada1computer(tabuleiro, simbM)
        x=VerificaVencedor(tabuleiro, simbH, nome)
        if x==1:
            mostraTabuleiro(tabuleiro)
            break
        mostraTabuleiro(tabuleiro)
else:
    tabuleiro=jogadaHumana(nome, simbH, tabuleiro)
    tabuleiro=jogada1computer(tabuleiro, simbM)
    mostraTabuleiro(tabuleiro)
    tabuleiro=jogadaHumana(nome, simbH, tabuleiro)
    tabuleiro=jogada1computer(tabuleiro, simbM)
    mostraTabuleiro(tabuleiro)
    tabuleiro=jogadaHumana(nome, simbH, tabuleiro)
    
