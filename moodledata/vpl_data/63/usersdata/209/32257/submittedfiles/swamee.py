# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('digite o valor f:'))
L=float(input('Digite o valor L:'))
Q=float(input('Digite o valor Q:'))
H=float(input('Digite o valor H:'))
V=float(input('digite o valor V:'))
g=9.81
e=0.000002
D=(8*f*L*(Q**2)/(math.pi**2)*g*H)**1/5
print('O valor D é %.4f'%D)
