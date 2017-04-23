# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
F= float(input('digite o valor de f:'))
L= float(input('digite o valor de l:'))
Q= float(input('digite o valor de q:'))
deltaH= float(input('digite o valor de delta h:'))
v=float(input('digite o valor de v:'))
g=9.81
e=0.000002
D=((8*F*L*(Q**2))/((math.pi**2)*g*deltaH))/(1/5)
Rey=(4*Q)/(math.pi*D*v)
K=0.25/((math.log10((e/(3.7*D))+(5.74/(Rey**(0.9))))))**2
print('d= %.4f' %D)
print('Rey= %.4f' %Rey)
print('K= %.4f' %K)
