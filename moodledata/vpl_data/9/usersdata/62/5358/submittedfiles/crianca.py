# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA

p1=input("Digite o valor de P1: ")
c1=input("Digite o valor de C1: ")
p2=input("Digite o valor de P2: ")
c2=input("Digite o valor de C2: ")

#PROCESSAMENTO/SAIDA

if p1*c1==p2*c2:
    print("0")
elif p1*c1>p2*c2:
    print("-1")
else:
    print("1")