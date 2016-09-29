# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f=input("digite f:")
L=input("digite o valor de L:")
Q=input("digite o valor de Q:")
DeltaH=input("digite o valor de DELTAH:")
v=input("digite o valor de v:")
D=((8*f*L*(Q**2))/((math.pi**2)*9.81*DeltaH))**0.2
Rey=(4*Q)/(math.pi*D*v)
x=0.000002/(3.7*D)
y=5.74/(Rey)**0.9
k=0.25/(math.log10(x+y))**2
print("D=%.4f" %D)
print("Rey=%.4f" %Rey)
print("k=%.4f" %k)