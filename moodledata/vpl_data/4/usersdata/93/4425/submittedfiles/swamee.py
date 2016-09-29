# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
F=input('F')
L=input('L')
Q=input('Q')
DeltaH=input('DeltaH')
V=input('V')
d=((8*F*L*Q**2)/((3.1416**2)*9.81*DeltaH))**0.2
rey=4*Q/(3.1416*D*V)
k=0.25/(math.log10((0.000002/(3.7*D)) + (5.74/Rey**0.9))
print('D==%.4f'%d)
print('Rey==%.4f'%rey)
print('K==%.4f'%k)

