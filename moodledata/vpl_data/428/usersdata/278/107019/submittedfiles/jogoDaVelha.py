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
    i=sorteio_i ()
    j=sorteio_j ()
    jc=jogadaComputador_1 (s,i,j,cont)
    mostraTabuleiro (jc)
    cont+=1
    while (cont<9):
        jh=jogadaHumana_2 (nome, s, jc, cont)
        mostraTabuleiro (jh)
        verificaVencedor (s,jh,nome,cont)
        #if cont
        cont+=1
        i=sorteio_i ()
        j=sorteio_j ()
        jc=jogadaComputador_2 (s,i,j,cont,jh)
        mostraTabuleiro (jc)
        verificaVencedor (s,jc,nome,cont)
        cont+=1
        
if sorteio==1:
    jh=jogadaHumana_1 (nome,s,cont)
    mostraTabuleiro (jh)
    cont+=1
    while (cont<9):
        i=sorteio_i ()
        j=sorteio_j ()
        jc=jogadaComputador_2 (s,i,j,cont,jh)
        mostraTabuleiro (jc)
        verificaVencedor (s,jc,nome,cont)
        cont+=1
        jh=jogadaHumana_2 (nome,s,jc,cont)
        mostraTabuleiro (jh)
        verificaVencedor (s,jh,nome,cont)
        cont+=1