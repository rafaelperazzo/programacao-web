# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f= input('Digite o valor de f: ')
L= input('Digite o valor de L: ')
Q= input('Digite o valor de Q: ')
DeltaH= input('Digite o valor de DH: ')
V= input('Digite o vaor de V: ')
g= 9.81
e= 0.000002
pi= 3.1415
D= ((8*f*L*(Q**2))/((pi**2)*g*DeltaH))**(1/5)
Rey= (4*Q)/(pi*D*V)
k= (0.25)/((math.log10(((e)/(3.7*D))+(5.74)/(Rey**0.9)))**2
print 'math.log'('%.4f'%D)
print 'math.log'('%.4f'%Rey)
print 'math log'('%.4f'%k)