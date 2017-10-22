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
    while int(x)!=0 or int(x)!=1 or int(x)!=2 and int(y)!=0 or int(y)!=1 or int(y)!=2:
        x, y= int(x), int(y)
        print('Coordenada invalida!')
        x, y=input('Digite sua primeira coordenada no intervalo (0,2):').split(',')
        x, y=int(x), int(y)
            print('matriz')
        break
else:
    print('Vencedor do sorteio para inicio do jogo: Computador')
    cord1pc=random.choice((0,1,2)),random.choice((0,1,2))
    print(cord1pc)
#lista1=(
#lista2=(
#lista3=(

#print(lista1)
#print(lista2)
#print(lista3)
    



    
        
        
   
