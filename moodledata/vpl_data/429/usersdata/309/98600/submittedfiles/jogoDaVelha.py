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
    
#sorteio da 1ª jogada    
sorteioPrimeiraJogada (simbM, simbH, tabuleiro, nome)

#função para pedir a jogada humana
tabJog=jogadaHumana(nome, simbH, tabuleiro)
#função para exibir tabuleiro
mostraTabuleiro(tabJog)
