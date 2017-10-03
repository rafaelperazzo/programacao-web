# -*- coding: utf-8 -*-
P1 = float(input("Digite o peso (kg) da criança à esquerda: "))
C1 = float(input("Digite o comprimento (m) do lado esquerdo: "))
P2 = float(input("Digite o peso (kg) da criança à direita: "))
C2 = float(input("Digite o comprimento (m) do lado direito: "))
v1=P1*C1
v2=P2*C2
if v1==v2:
    print("0")
if v1>v2:
    print("-1")
if v1<v2:
    print("1")


