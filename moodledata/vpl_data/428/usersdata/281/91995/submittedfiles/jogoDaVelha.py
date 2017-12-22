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
    n=random.choice(('00','01','02','10','11','12','20',21,'22'))
    n=print(n)

if sort==1 and n=='00' and simb=='O':
    quadro(['O',' ',' ',' ',' ',' ',' ',' ',' ',' '])
elif sort==0 and n=='01' and simb=='O':
    quadro([' ','O',' ',' ',' ',' ',' ',' ',' ',' '])
elif sort==0 and n=='02' and simb=='O':
    quadro(['O',' ',' ',' ',' ',' ',' ',' ',' ',' '])


    



    
        
        
   
