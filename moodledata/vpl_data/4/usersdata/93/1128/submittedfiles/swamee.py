# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
F=input('F')
L=input('L')
Q=input('Q')
deltaH=input('deltaH')
V=input('V')

Rey=4*Q/(3.1416*D*V)
K=0.25/(math.log10((0.000002/(3.7*D)) + (5.74/Rey**0.9))

print('%.4f'%Rey)
print('%.4f'%K)
