# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('digite f:'))
L=float(input('digite L:'))
Q=float(input('digite Q:'))
DH=float(input('digite DH:'))
v=float(input('digite v:'))
D=(8*f*L*(Q**2))/((math.pi**2)*9.81*DH)**(1/5)
REY=4*Q/math.pi*D*v
k=0.25/(math.log10((0.000002/3.7*D)+(5.74/REY**(0.9))))**2
print('D é %.4f'%D)
print('REY é %.4f'%REY)
print('k é %.4f'%k)