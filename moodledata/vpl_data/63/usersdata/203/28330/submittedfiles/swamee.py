# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
pi=math.pi
g=9.81
E=0.000002
f=float(input('Digite f:'))
L=float(input('Digite L:'))
Q=float(input('Digite Q:'))
deltaH=float(input('Digite deltaH:'))
v=float(input('Digite v:'))
D=((8*f*L*Q*Q)**(1/5))/((pi*pi*g*deltaH)**(1/5))
Rey=(4*Q)/(pi*D*v)
k=0.25/(math.log10(E/(3.7*D)+5.74/(Rey**0.9)))**2
print('D= %.4f' %D)
print('Rey= %.4f' %Rey)
print('k= %.4f' %k)