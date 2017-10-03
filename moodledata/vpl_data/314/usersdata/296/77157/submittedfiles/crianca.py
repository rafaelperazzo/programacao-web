# -*- coding: utf-8 -*-
P1 = float(input("Digite o peso do lado esquerdo: "))
C1 = float(input("Digite o comprimento do lado esquerdo: "))
P2 = float(input("Digite o peso do lado direito: "))
C2 = float(input("Digite o comprimento do lado direito: "))
if P1*C1==P2*C2:
    print("0")
else P1 * C1>P2*C2:
    print("-1")
else P1 * C1<P2*C2:
    print("1")


