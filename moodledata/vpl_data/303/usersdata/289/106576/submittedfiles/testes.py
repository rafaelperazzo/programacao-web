# -*- coding: utf-8 -*-
from minha_bib import *

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
    while (cont<=9):
        jh=jogadaHumana_2 (nome, s, jc, cont)
        mostraTabuleiro (jh)
        cont+=1
        i=sorteio_i ()
        j=sorteio_j ()
        jc=jogadaComputador_2 (s,i,j,cont,jh)
        mostraTabuleiro (jc)
        cont+=1
        
if sorteio==1:
    jh=jogadaHumana_1 (nome,s,cont)
    mostraTabuleiro (jh)
    cont+=1
    while (cont<=9):
        i=sorteio_i ()
        j=sorteio_j ()
        jc=jogadaComputador_2 (s,i,j,cont,jh)
        mostraTabuleiro (jc)
        jh=jogadaHumana_2 (nome,s,jc,cont)
        cont+=1
if jogada=='00'and jogada=='01' and  jogada=='02':
    print("vc venceu")
if jogada=='10' and jogada=='11' and jogada=='12':
    print("vc venceu")
if jogada=='20' and jogada=='21' and jogada=='22':
    print("vc venceu")
if jogada=='00' and jogada=='10' and jogada=='20':
    print("vc venceu")
if jogada=='01' and jogada=='11' and jogada=='21':
    print("vc venceu")
if jogada=='02' and jogada=='12' and jogada=='22':
    print("vc venceu")
if jogada=='00' and jogada=='11' and jogada=='22':
    print("vc venceu")
if jogada=='02' and jogada=='11' and jogada=='20':
    print("vc venceu")
        
