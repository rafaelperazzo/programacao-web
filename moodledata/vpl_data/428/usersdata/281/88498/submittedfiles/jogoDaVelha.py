# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *
import random  
# COLOQUE SEU PROGRAMA A PARTIR DAQUI

print('Bem vindo ao Jogo da Velha da equipe ESSI')
nome=str(input('Qual o seu nome (ou apelido)? '))
simb ()
sort=random.choice((1,0))
if sort==1:
    print('Vencedor do sorteio para inicio do jogo: Voce')
    cord1=int(input('Digite sua primeira coordenada no intervalo [0,2]:'))
else:
    print('Vencedor do sorteio para inicio do jogo: Computador')
    cor1pc=(random.choice((0,2)),random.choice((0,2)))
    



    
        
        
   
