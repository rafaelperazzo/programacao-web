# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
lista0=[' ', ' ', ' ']
lista1=[' ', ' ', ' ']
lista2=[' ', ' ', ' ']
m=[]
m.append(lista0)
m.append(lista1)
m.append(lista2)
print("Bem vindo ao JogoDaVelha do grupo E")
nome = str(input("Qual o seu nome (ou apelido)? "))
s = simbolo_escolhido ()
if s=='X':
    X='humano'
    O='computador'
sorteio = sorteio ()
i=sorteio_i ()
j=sorteio_j ()
if s=='X':
    jogadaComputador (sorteio_i,sorteio_j)
mostraTabuleiro (m)
            