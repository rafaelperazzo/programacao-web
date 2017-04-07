# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('Digite o valor de f:'))
L=float(input('Digite o valor de L:'))
Q=float(input('Digite o valor de Q:'))
DeltaH=float(input('Digite o valor de DeltaH:'))
v=float(input('Digite o valor de v:'))
g=9.81
e=0.000002
d=((8*f*L)*(Q**2))/((math.pi**2)*g*DeltaH))**(1/5)
Rey=(4*Q)/(math.pi*d*v)
k=0.25/(math.log10((e/3.7*d)+(5.74/((Rey)**0.9))))**2
print('%.4f' %d)
print('O valor de Rey é: %.4f' %Rey)
print('O valor de k é: %.4f' %k)