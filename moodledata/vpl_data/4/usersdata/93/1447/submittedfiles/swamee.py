# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
F=input('F')
L=input('L')
Q=input('Q')
deltaH=input('deltaH')
V=input('V')
D=((8*F*L*Q**2)/((3.1416**2)*9.81*deltaH))**0.5
Rey=4*Q/(3.1416*D*V)
K=0.25/(math.log10((0.000002/(3.7*D)) + (5.74/Rey**0.9))
print('D =%.4f'%D)
print('Rey = %.4f'%Rey)
print('K= %.4f'%K)

