# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
print("Bem vindo ao JogoDaVelha do grupo E")
nome = str(input("Qual o seu nome (ou apelido)? "))
s = simbolo_escolhido ()
if s=="X":
    X="humano"
    O="computador"
sorteio = sorteio ()
if sorteio=="computador":
    print("   |   |   ")
    if s=="X":
        print("   | O |   ")
    if s=="O":
        print("   | X |   ")
    print("   |   |   ")
    
