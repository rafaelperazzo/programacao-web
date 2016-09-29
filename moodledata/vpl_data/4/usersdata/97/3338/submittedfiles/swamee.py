# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f=input('Digite o valor de f:')
L=input('Digite o valor de L:')
Q=input('Digite o valor de Q:')
deltaH=input('Digite o valor de deltaH:')
v=input('Digite o valor de v:')

D=((8*f*L*(Q**2))/((math.pi**2)*9.81*deltaH))
Rey=(4*Q)/(math.pi*D*v)
k=(0.25)/(math.log((0.000002/3.7*D)+(5.74/Rey**0.9)))**2

print('D=:%.4f ,Rey=%.4f ,k=%.4f'%D,Rey,k)





