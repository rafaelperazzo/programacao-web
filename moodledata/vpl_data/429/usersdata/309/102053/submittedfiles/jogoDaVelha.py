# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *


#definindo o tabuleiro 
tabuleiro=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

#nome do jogador
nome=input('Qual seu nome(ou apelido)? ')
#chamando a função da soli. do simbolo humano  
simbH=solicitaSimboloDoHumano()

# definição do simbolo da máquina
if simbH=="x" or simbH=="X":
        simbM="O"
else:
    simbM="X"
    
#sorteio da 1ª jogada, e definição de quem fará a próxima jogada    
prop=sorteioPrimeiraJogada (simbM, simbH, tabuleiro, nome)


#Condição para definir as jogadas posteriores 
if prop==1:
    #função para pedir a jogada humana
    tabJog=jogadaHumana(nome, simbH, tabuleiro)
    #função para exibir tabuleiro
    mostraTabuleiro(tabJog)
else:
    
    tabuleiro=jogadaHumana(nome, simbH, tabuleiro)
    tabjog=jogada1computer(tabuleiro, simbM)
    mostraTabuleiro(tabJog)
