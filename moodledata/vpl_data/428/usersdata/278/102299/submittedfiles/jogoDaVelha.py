# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
print("Bem vindo ao JogoDaVelha do grupo E")
nome = str(input("Qual o seu nome (ou apelido)? "))
s = simbolo_escolhido ()
if s=='X':
    X='humano'
    O='computador'
sorteio = sorteio ()
if sorteio==2:
    i=sorteio_i ()
    j=sorteio_j ()
    m=jogadaComputador (s,i,j)
    mostraTabuleiro (m)
        
            