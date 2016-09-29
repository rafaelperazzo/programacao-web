# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI

#Entrada

f = float(input('Digite o valor de f; '))
L= int(input('Digite o valor de L: '))
Q = float(input('Digite o valor de q: '))
DeltaH = int(input('Digite o valor de DeltaH: '))
v = float(input('Digite o valor de V: '))

#Processamento
Dp1 = 8.0000 * f * L * (q**2)
print(Dp1)
Dp2 = (math.pi**2) * (9.81) * (DeltaH)
print(Dp2)
D = (Dp1/Dp2)**(0.2)

Rey = (4*Q)/(math.pi*D*v)

K = (0.25)/(math.log10((0.000002/3.7*D) + (5.74/Rey**0.9)))**2

#Saida

print('D = ') +str(D)

print('Rey = ') +str(Rey)

print('K = ') +str(K)
