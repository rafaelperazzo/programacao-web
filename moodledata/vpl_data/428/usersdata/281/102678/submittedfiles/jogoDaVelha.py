# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *
import random  
# COLOQUE SEU PROGRAMA A PARTIR DAQUI

print('Bem vindo ao Jogo da Velha da equipe ESSI')
nome=str(input('Qual o seu nome (ou apelido)? '))
simb=simb ()
sorteio=sorteio ()
if sorteio==1:
    print('Vencedor do sorteio para inicio do jogo: ' +nome  )
    #jogadahumano()
if sorteio==0:
    print('Vencedor do sorteio para inicio do jogo: Computador' )
    jogadapc ()
    
    




       
    


    



    
        
        
   
