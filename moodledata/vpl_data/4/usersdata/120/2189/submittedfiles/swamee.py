# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA
f=input('digite o valor de f:')
l=input('digite o valor de l:')
Q=input('digite o valor de Q:')
Deltah=input('digite o valor de Deltah:')
v=input('digite o valor de v:')
#PROCESSAMENTO
D=((8*f*l*(Q**2))/((math.pi**2)*9.81*Deltah))**(0.2)
Rey=(4*Q)/(math.pi*D*v)
K=0.25/(math.log10((0.000002/3.7*D)+(5.74/Rey**0.9)))**2
#SAIDA
print('D%.4f='%D)
print('Rey%.4f='%Rey)
print('K%.4f='%K)
