# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
#entrada
f=input('digite o valor de f:')
L=input('digite o valor de L:')
Q=input('digite o valor de Q:')
deltaH=input('digite o valor de deltaH:')
v=input('digite o valor de v:')
#processamento 
D=((8*f*L*(Q**2))/((math.pi**2)*9.81*deltaH))**1/5
rey=(4*Q)/((math.pi)*D*v)
k=(0.25)/((math.log10(0.000002/(3.7*D)+5.74/(rey**0.9)))**2
#saida
print('D=%.4f'%D)
print('Rey=%.4f'%rey)
print('k=%.4f'%k)