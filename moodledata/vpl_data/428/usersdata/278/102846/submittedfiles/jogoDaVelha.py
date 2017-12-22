# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
cont=0
print("Bem vindo ao JogoDaVelha do grupo E")
nome = str(input("Qual o seu nome (ou apelido)? "))
s = simbolo_escolhido ()
if s=='X':
    X='humano'
    O='computador'
sorteio = sorteio (nome)
if sorteio==2:
    while (cont<=9):
        i=sorteio_i ()
        j=sorteio_j ()
        m=jogadaComputador (s,i,j)
        mostraTabuleiro (m)
        cont+=1
        c=jogadaHumana (nome, s, m)
        mostraTabuleiro (m)
        cont+=1
        
if sorteio==1:
    while (cont<=9):
        c=jogadaHumana (nome, s, lista0, lista1, lista2)
        mostraTabuleiro (m)
        cont+=1
        i=sorteio_i ()
        j=sorteio_j ()
        m=jogadaComputador (s,i,j)
        mostraTabuleiro (m)
        cont+=1