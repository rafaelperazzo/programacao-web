# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *


#definido o tabuleiro 
tabuleiro=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#nome do jogador
nome=input('Qual seu nome(ou apelido)? ')
simbH=solicitaSimboloDoHumano()
tabJog=jogadaHumana(nome, simbH, tabuleiro)
mostraTabuleiro(tabJog)
