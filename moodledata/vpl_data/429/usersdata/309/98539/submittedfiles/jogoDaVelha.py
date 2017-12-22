# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *


#definido o tabuleiro 
tabuleiro=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#nome do jogador
nome=input('Qual seu nome(ou apelido)? ')
simbH=solicitaSimboloDoHumano()
#função para pedir a jogada humana
tabJog=jogadaHumana(nome, simbH, tabuleiro)
#função para exibir tabuleiro
mostraTabuleiro(tabJog)
