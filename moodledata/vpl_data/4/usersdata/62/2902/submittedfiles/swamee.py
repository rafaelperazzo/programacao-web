# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
#ENTRADA

f=input("valor de f: ")
L=input("valor de L: ")
Q=input("valor de Q: ")
DeltaH=input("valor de DeltaH: ")
v=input("valor de v: ")

#PROCESSAMENTO
g=9.81
e=0.000002
D=(8*f*L*(Q**2)/((math.pi**2)*g*DeltaH))**0.2
Rey=4*Q/(math.pi*D*v)
k=0.25/(math.log10(e/(3.7*D)+(5.74/Rey**0.9)))**2

#SAIDA

print("D=%.4f"%D)
print('rey=%.4f'%Rey)
print('k=%.4f'%k)