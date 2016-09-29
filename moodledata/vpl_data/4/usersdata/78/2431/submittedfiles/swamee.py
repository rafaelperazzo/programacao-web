# -*- coding: utf-8 -*-
from __future__ import division
import math

f=input('digite o valor de f')
L=input('digite o valor de l')
Q=input('digite o valor de q')
DeltaH=input('digite o valor de Deltah')
v=input('digite o valor de v')

D=((8*f*L*(Q**2))/(((math.pi)**2)*9.81*DeltaH))**0.2
Rey=(4*Q)/((math.pi)*D*v)
K=0.25/(math.log10((0.000002/(3.7*D))+(5.74/(Rey**0.9))))

print('%.4f' %D)
print('%.4f' %Rey)
print('%.4f' %K)
