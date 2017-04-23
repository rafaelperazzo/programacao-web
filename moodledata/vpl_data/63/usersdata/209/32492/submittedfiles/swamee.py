# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('digite o valor f:'))
L=float(input('Digite o valor L:'))
Q=float(input('Digite o valor Q:'))
DELTAH=float(input('Digite o valor DELTAH:'))
V=float(input('digite o valor V:'))
g=9.81
e=0.000002
D=((8*f*L*(Q**2))/((math.pi**2)*g*DELTAH))**(1/5)
Rey=((4*Q)/(math.pi*D*V))
k=(0.25/(math.log10((e/3.7*D)+(5.74/Rey**0.9)))**2
print('O valor D é %.4f'%D)
print('O valor Rey é %.4f'%Rey)
print('O valor k é %f'%k)