# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
#ENTRADA

f=input("valor de f: ")
L=input("valor de L: ")
Q=input("valor de Q: ")
deltaH=input("valor de DeltaH: ")
v=input("valor de v: ")

#PROCESSAMENTO
g=9.81
e=0.000002
D=((8*f*L*(Q**2))/((math.pi**2)*g*deltaH))**0.2
rey=(4*Q)/((math.pi)*D*v)
k=(0.25)/(((math.log10((e/(3.7*D))+(5.74/(rey**0.9)))**2)

#SAIDA

print('D=%.4f'%D)
print('rey=%.4f'%rey)
print('k=%.4f'%k)