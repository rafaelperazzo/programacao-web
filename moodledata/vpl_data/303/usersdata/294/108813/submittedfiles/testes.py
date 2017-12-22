# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
from jogoDaVelha_BIB import *
    3 import time
    4 # COLOQUE SEU PROGRAMA A PARTIR DAQUI
    5 cont=0
    6 print("Bem vindo ao JogoDaVelha do grupo E")
    7 time.sleep(1)
    8 nome=str(input("Qual o seu nome (ou apelido)? "))
    9 time.sleep(1)
   10 s=simbolo_escolhido ()
   11 time.sleep(1)
   12 sorteio=sorteio (nome)
   13 time.sleep(1)
   14 if sorteio==2:
   15     i=sorteio_i ()
   16     j=sorteio_j ()
   17     jc=jogadaComputador_1 (s,i,j,cont)
   18     mostraTabuleiro (jc)
   19     print('\n')
   20     cont+=1
   21     while (cont<9):
   22         time.sleep(2)
   23         jh=jogadaHumana_2 (nome, s, jc, cont)
   24         mostraTabuleiro (jh)
   25         print('\n')
   26         time.sleep(1)
   27         vv=verificaVencedor (s,jh,nome,cont)
   28         if vv==10:
   29             break
   30         cont+=1
   31         if cont<9:
   32             while (jh[i][j]!=' '):
   33                 i=sorteio_i ()
   34                 j=sorteio_j ()
   35             time.sleep(1)
   36             jc=jogadaComputador_2 (s,i,j,cont,jh)
   37             mostraTabuleiro (jc)
   38             print('\n')
   39             time.sleep(1)
   40             vv=verificaVencedor (s,jc,nome,cont)
   41             if vv==10:
   42                 break
   43             cont+=1
   44     if cont==9:
   45         print('Deu velha')
   46 if sorteio==1:
   47     jh=jogadaHumana_1 (nome,s,cont)
   48     mostraTabuleiro (jh)
   49     print('\n')
   50     cont+=1
   51     while (cont<9):
   52         i=sorteio_i ()
   53         j=sorteio_j ()
   54         while (jh[i][j]!=' '):
   55                 i=sorteio_i ()
   56                 j=sorteio_j ()
   57         time.sleep(2)
   58         jc=jogadaComputador_2 (s,i,j,cont,jh)
   59         mostraTabuleiro (jc)
   60         print('\n')
   61         time.sleep(1)
   62         vv=verificaVencedor (s,jc,nome,cont)
   63         if vv==10:
   64             break
   65         cont+=1
   66         if cont<9:
   67             time.sleep(1)
   68             jh=jogadaHumana_2 (nome,s,jc,cont)
   69             mostraTabuleiro (jh)
   70             print('\n')
   71             time.sleep(1)
   72             vv=verificaVencedor (s,jh,nome,cont)
   73             if vv==10:
   74                 break
   75             cont+=1
   76     if cont==9:
   77         print('Deu velha')