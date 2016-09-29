# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
#Entrada

f=('Digite o valor de f:')
L=('Digite o valor de L:')
Q=('Digite o valor de Q:')
DeltaH=('Digite o valor de deltaH:')
v=('Digite o valor de v:')

#Processamento
g=9.81
e=0.000002

D=((8*f*L*(Q**2))/((math.pi**2)*g*DeltaH))**1/5

#Saída
print ('%.4f'%(D))