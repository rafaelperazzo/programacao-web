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
    
    
else:
    print('Vencedor do sorteio para inicio do jogo: Computador')
    n=random.choice((00,11,22)),random.choice((0,1,2))
    print(n)


if sort==0:
    quadro([' ','O',' ',' ',' ',' ',' ',' ',' ',' '])

else:
    n=int(input('qual a sua jogada?'))
if n==00 and simb=='X':
    quadro(['X','O',' ',' ',' ',' ',' ',' ',' ',' '])
    
    



    
        
        
   
