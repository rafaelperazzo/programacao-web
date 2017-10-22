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
    xvc,yvc=input('Digite sua primeira coordenada no intervalo (0,2):')
    xvc,yvc= int(xvc), int(yvc)
    print('matriz')
else:
    print('Vencedor do sorteio para inicio do jogo: Computador')
    xpc,ypc=random.choice((0,1,2)),random.choice((0,1,2))
    print('matriz')
    



    
        
        
   
