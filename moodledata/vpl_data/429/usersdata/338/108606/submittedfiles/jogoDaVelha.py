# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
import random
from time import sleep
import jogoDaVelha_BIB
#######################################################################################

#######################################################################################

coordenadas = [
            ('00', '01', '02')
            ,('10', '11','12')  #Matriz das coordenadas
            ,('20','21','22')
            ]

tabuleiro = [
            (' ', ' ', ' ')
            ,(' ', ' ', ' ')  #matriz tabuleiro
            ,(' ', ' ', ' ')
            ]
tabuleiro = []
for i in range (3):
    v = []
    for j in range(3):
        v.append(' ')
    tabuleiro.append(v)

nome_do_jogador = input("Digite o seu nome: ") #Pede o nome do jogador
simb = input('Digite o simbolo com o qual você deseja jogar %s : ' % nome_do_jogador)
while(True):   #Verifica se o simbolo é vàlido
    if simb == "X" or simb == "O" :
        break
    else:
        simb = input("Digite um simbolo válido %s : " % nome_do_jogador)
    

if simb == 'X':
    simbc = 'O'
else:
    simbc = 'X'

print('Agora sortearemos quem começará: ')
sleep(1.5)

a = (random.choice(['1','2']))

if a == 1:
    print('Você começa: ')
    while(True) :
        if verifica_vencedor() :
            break   
        else:
            mostre_tabuleiro()
            recebe_e_validar_jogada()
            jogada_do_computador()
            mostre_tabuleiro()
    

else:
    print('O computador começou')
    while(True):
        if verifica_vencedor() :
            break
        else:
            jogada_do_computador() 
            mostre_tabuleiro()
            recebe_e_validar_jogada()
    
    
        
    





        
        
        
        
        
        