# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
F=input('F')
L=input('L')
Q=input('Q')
DeltaH=input('DeltaH')
V=input('V')
d=((8*F*L*Q**2)/((math.pi**2)*9.81*DeltaH))**0.2
rey=4*Q/(math.pi*d*V)
k=0.25/(math.log10((0.000002/(3.7*d)) + (5.74/rey**0.9))**2)
print("'D=%.4f'"%d)
print("'Rey=%.4f'"%rey)
print("'k=%.4f'"%k)

