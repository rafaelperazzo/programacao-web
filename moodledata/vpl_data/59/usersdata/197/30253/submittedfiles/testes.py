# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
F=float(input('Digite o valor de f:'))
L=float(input('Digite o valor de L:'))
Q=float(input('Digite o valor de Q:'))
DELTAH=float(input('Digite o valor de DELTAH:'))
V=float(input('digite o valor de V:'))
g=9.81
e=0.000002
D=(((8*F*L*Q*Q)/(math.pi**2*g*DELTAH))**1/5)
Rey=((4*Q)/(math.pi*D*V))
K=((0.25)/(math.log10((e/3.70)+(5.74)/Rey**0.9)))**2
print('%.4f'%D)
print('%.4f'%Rey)
print('%.4f'%K)