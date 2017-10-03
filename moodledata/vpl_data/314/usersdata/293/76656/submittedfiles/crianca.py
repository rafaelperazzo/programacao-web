# -*- coding: utf-8 -*-
P1=float(input("Peso da esquerda: "))
C1=float(input("Comprimento da esquerda: "))
P2=float(input("Peso da direita: "))
C2=float(input("Comprimento da direita: "))

K1=P1*C1
K2=P2*C2
if K1==K2:
    print("0")
elif K1>K2:
    print("-1")
else: 
    print("1")
    
    
