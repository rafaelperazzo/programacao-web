# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
#ENTRADA
f=input('Digite o valor de f:')
L=input('Digite o valor de L:')
Q=input('Digite o valor de Q:')
DeltaH=input('Digite o valor de DeltaH:')
v=input('Digite o valor de v:')

#PROCESSAMENTO
g=(9.81)
e=(0.000002)

D=(((8.0*f*L*((Q)**2.0))/float(((math.pi)**2.0)*g*DeltaH))**(0.2))

Rey=((4.0*Q)/float((math.pi)*D*v))

k=((0.25)/float((math.log((e/float(3.7*D))+(5.74/float(Rey**0.9))))**2))

#SAIDA
print('O valores de D, Rey e k são, respectivamente, %.4f, %.4f e %.4f ' %(D,Rey,k))










