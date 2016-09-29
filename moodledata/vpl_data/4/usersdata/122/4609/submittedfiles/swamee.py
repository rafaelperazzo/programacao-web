# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA

f=input('Digite o valor de f:')
L=input('Digite o valor de L:')
Q=input('Digite o valor de Q:')
H=input('Digite o valor de H:')
v=input('Digite o valor de v:')

#PROCESSAMENTO

D=8*f*L*(Q**2)/(((math.pi))**2*9.81*H)**(1/5)
Rey=(4*Q)/(math.pi)*D*v
K=0.25/(math.log10((0.000002/3.7*D)+(5.74/Rey**0.9)))

#SAÍDA

print(D)
print(Rey)
print(K)