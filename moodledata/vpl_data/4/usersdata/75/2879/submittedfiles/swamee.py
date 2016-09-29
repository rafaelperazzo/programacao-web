# -*- coding: utf-8 -*-
from __future__ import division
import math

#Entrada
f=input ('Digite o valor de f:')
L=input ('Digite o valor de l:')
Q=input ('Digite o valor de Q:')
deltaH=input ('Digite o valor de Delta:')
v=input ('Digite o valor de v:')

#Processamento 

D=(8*f*l*(Q**2)/((math.pi**2)*9,81*deltaH))**0.2
Rey=(4*Q)/(math.pi*D*v)
k=0,25/(math.log10((o,ooooo2/(3,7*D))+(5,74/Rey**0,9)))**2

#Saida
print ('D=%.4f'%(D))
print ('Rey=%.4f'%(Rey))
print ('k=%.4f'%(k))