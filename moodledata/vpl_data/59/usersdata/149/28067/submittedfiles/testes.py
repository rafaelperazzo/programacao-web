# -*- coding: utf-8 -*-
import math
f=float(input('digite o valor de f:'))
L=float(input('digite o valor de L:'))
Q=float(input('digite o valor de Q:'))
DeltaH=float(input('digite o valor de deltaH:'))
g=float(9.81)
e=float(0.000002)
D=float(5.6098)
rey=float(12.8932)
K=(0.25)/((math.log10(e/(3.7*D))*(5.74/(rey**0.9))))**2
print('%.4f'%D) 
