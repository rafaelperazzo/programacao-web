# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *
import random  
# COLOQUE SEU PROGRAMA A PARTIR DAQUI

print('Bem vindo ao Jogo da Velha da equipe ESSI')
nome ()
simb ()
sort=random.choice((1,0))
if sort==1:
    print('Vencedor do sorteio para inicio do jogo: '+nome ()+' ' )
    
    
else:
    print('Vencedor do sorteio para inicio do jogo: Computador')
    
if sort==1:
    jogada_humana ()
    
else:
    print('0')
    


    



    
        
        
   
