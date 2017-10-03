# -*- coding: utf-8 -*-
P1 = float(input("Peso 1: "))
C1 = float(input("Comprimento 1: "))
P2 = float(input("Peso 2: "))
C2 = float(input("Comprimento 2: "))
#PROCESSAMENTO
if P1*C1==P2*C2:
    print("0")
if P1*C1<P2*C2:
    print("1")
if P1*C1>P2*C2:
    print("-1")
