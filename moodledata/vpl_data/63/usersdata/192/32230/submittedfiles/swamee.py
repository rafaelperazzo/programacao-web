# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

f=float(input('Digite f:'))
l=float(input('Digite l:'))
q=float(input('Digite q:'))
h=float(input('Digite h:'))
v=float(input('Digite v:'))
D=((8*f*l*(q**2))/math.pi**2*9.81*h))**(1/5)
R=(4*q)/(math.pi.D*v)
K=0.25/((math.loh10(0.000002/(3.7*D)+(5.75/(R**0.9))))**2)
print('D: %.4f'%D)
print('R: %.4f'%R)
print('K: %.4f'%K)