# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('Digite aqui o valor de f:'))
L=float(input('Digite aqui o valor de L:'))
Q=float(input('Digite aqui o valor de Q:'))
DeltaH=float(input('Digite o valor de Delta H:'))
v=float(input('Digite o valor de v:'))
g=9.81
E=0.000002
Pi=3.14159
D=((8*f*L*(Q*Q))/((Pi*Pi)*g*DeltaH))**(1/5)
Rey=4*Q/(math.pi*D*v)
k=(0.25)/(math.log10((E/(3.7*D))+(5.74/(Rey*0.9))))**2
print('%.4f'%D)
print('%.4f'%Rey)
print('%.4f'%k)
