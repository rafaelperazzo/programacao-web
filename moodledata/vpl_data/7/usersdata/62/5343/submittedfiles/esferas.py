# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
a=input("Digite o valor de A: ")
b=input("Digite o valor de B: ")
c=input("Digite o valor de C: ")
d=input("Digite o valor de D: ")

#PROCESSAMENTO

if a==b+c+d and b+c==d and b==c:
    print("S")
else:
    print("N")
    