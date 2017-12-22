# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *
import time
# COLOQUE SEU PROGRAMA A PARTIR DAQUI
cont=0
print("Bem vindo ao JogoDaVelha do grupo E")
time.sleep(1)
while (resposta=='sim'):
    nome = str(input("Qual o seu nome (ou apelido)? "))
    time.sleep(1)
    s = simbolo_escolhido ()
    time.sleep(1)
    sorteio = sorteio (nome)
    time.sleep(1)
    if sorteio==2:
        i=sorteio_i ()
        j=sorteio_j ()
        jc=jogadaComputador_1 (s,i,j,cont)
        mostraTabuleiro (jc)
        cont+=1
        while (cont<9):
            time.sleep(2)
            jh=jogadaHumana_2 (nome, s, jc, cont)
            mostraTabuleiro (jh)
            vv=verificaVencedor (s,jh,nome,cont)
            if vv==10:
                break
            cont+=1
            if cont<9:
                while (jh[i][j]!=' '):
                    i=sorteio_i ()
                    j=sorteio_j ()
                time.sleep(2)
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
        if cont==9:
            print('Deu velha')
            
    if sorteio==1:
        jh=jogadaHumana_1 (nome,s,cont)
        mostraTabuleiro (jh)
        cont+=1
        while (cont<9):
            i=sorteio_i ()
            j=sorteio_j ()
            while (jh[i][j]!=' '):
                    i=sorteio_i ()
                    j=sorteio_j ()
            time.sleep(2)
            jc=jogadaComputador_2 (s,i,j,cont,jh)
            mostraTabuleiro (jc)
            vv=verificaVencedor (s,jc,nome,cont)
            if vv==10:
                break
            cont+=1
            if cont<9:
                time.sleep(2)
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
        if cont==9:
            print('Deu velha')
    resposta=bool(input('Deseja jogar novamente? '))
    if resposta=='nao':
        break
        