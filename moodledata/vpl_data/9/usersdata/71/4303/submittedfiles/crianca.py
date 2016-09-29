# -*- coding: utf-8 -*-
from __future__ import division

p1=input("Insira o peso esquerdo: ")
c1=input("Insira o comprimento esquerdo: ")
p2=input("Insira o peso direito: ")
c2=input("Insira o comprimento direito: ")

if p1*c1==p2*c2:
    print("0")
elif p1*c1<=p2*c2:
    print("1")
elif p1*c1>=p2*c2:
    print("-1")