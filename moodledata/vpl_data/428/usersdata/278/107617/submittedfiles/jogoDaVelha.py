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
        vv=verificaVencedor (s,jh,nome,cont)
        if vv==10:
            break
        cont+=1
        if cont<9:
            i=sorteio_i ()
            j=sorteio_j ()
            jc=jogadaComputador_2 (s,i,j,cont,jh)
            mostraTabuleiro (jc)
            vv=verificaVencedor (s,jc,nome,cont)
            if vv==10:
                break
            cont+=1
            if cont<9:
                continue
            else:
                break
        else:
            break
    print('Deu velha')
        
if sorteio==1:
    jh=jogadaHumana_1 (nome,s,cont)
    mostraTabuleiro (jh)
    cont+=1
    while (cont<9):
        i=sorteio_i ()
        j=sorteio_j ()
        jc=jogadaComputador_2 (s,i,j,cont,jh)
        mostraTabuleiro (jc)
        vv=verificaVencedor (s,jc,nome,cont)
        if vv==10:
            break
        cont+=1
        if cont<9:
            jh=jogadaHumana_2 (nome,s,jc,cont)
            mostraTabuleiro (jh)
            vv=verificaVencedor (s,jh,nome,cont)
            if vv==10:
                break
            cont+=1
            if cont<9:
                continue
            else:
                break
        else:
            break
    if vv!=10:
        print('Deu velha')
        