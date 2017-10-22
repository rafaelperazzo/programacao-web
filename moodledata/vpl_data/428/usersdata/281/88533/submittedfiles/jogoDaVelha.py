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
    x, y=input('Digite sua primeira coordenada no intervalo (0,2):').split(',')
    if x==0 or x==1 or x==2 and y==0 or y==1 or y==2:
        x, y= int(x), int(y)
        print('matriz')
    else:
        print('Coordenada invalida!')
else:
    print('Vencedor do sorteio para inicio do jogo: Computador')
    cord1pc=random.choice((0,1,2)),random.choice((0,1,2))
    print(cord1pc)
    



    
        
        
   
