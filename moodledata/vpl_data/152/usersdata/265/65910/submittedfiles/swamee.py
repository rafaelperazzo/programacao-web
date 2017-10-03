# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f = float(input('digite o valor de f: '))
L = float(input('digite o valor de L: '))
Q = float(input('digite o valor de Q: '))
DeltaH = float(input('digite o valor de DeltaH: '))
Omega = float(input('digite o valor de Omega: '))
g = 9.81
E = 0.000002
PI = math.pi
D = ((8*f*L*(Q**2))/((PI**2)*g*DeltaH))**(1/5)
Rey = (4*Q)/(PI*D*Omega)
K = (0.25)/((math.log10((E/(3.7*D))+(5.47/(Rey**0.9))))**2)
print('%.4f' %D)
print('%.4f' %Rey)
print('%.4f' %K)