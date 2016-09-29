# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f=input("digite f")
L=input("digite o valor de L")
Q=input("digite o valor de Q")
DELTAH=input("digite o valor de DELTAH")
v=input("digite o valor de v")
D=
Rey=(4*Q)/(math.pi*D*v)
x=0.000002/(3.7*D)
y=5.74/(Rey)**0.9
k=0.25/(math.log10(x+y))**2
print("o valor de D eh:%.4f" %D)
print("o valor de Rey eh:%.4f" %Rey)
print("o valor de k eh:%.4f" %k)