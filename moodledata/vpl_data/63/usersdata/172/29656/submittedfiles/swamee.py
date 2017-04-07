# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('Digite o valor de f:'))
l=float(input('Digite o valor de l:'))
q=float(input('Digite o valor de q:'))
dh=float(input('Digite o valor de dh:'))
v=float(input('Digite o valor de v: '))
£=0.000002
D=(((8*f*l*(q*q)))/(((math.pi)**2)*9.81*dh))**(1/5)
Rey=((4*q)/(math.pi*D*v))
print('D= %.4f'%D)
print('Rey= %.4f'%Rey)
