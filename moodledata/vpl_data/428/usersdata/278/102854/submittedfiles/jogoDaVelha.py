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
        k=jogadaComputador (s,i,j,cont)
        mostraTabuleiro (k)
        cont+=1
        c=jogadaHumana (nome, s, k, cont)
        mostraTabuleiro (c)
        cont+=1
        
if sorteio==1:
    while (cont<=9):
        m=[]
        n=jogadaHumana (nome, s, m, cont)
        mostraTabuleiro (n)
        cont+=1
        i=sorteio_i ()
        j=sorteio_j ()
        l=jogadaComputador (s,i,j,cont)
        mostraTabuleiro (l)
        cont+=1