# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

f=float(input('Digite F: '))
l=float(input('Digite l: '))
q=float(input('Digite q: '))
h=float(input('Digite h: '))
v=float(input('Digite v: '))
D=((8*f*l*(q**2))/(math.pi**2*9.81*h))**(1/5)
R=(4*q)/(math.pi*D*v)
K=0.25/((math.log10(0.000002/(3.7*D)+(5.74/(R**0.9))))**2)
print('%.4f'%D)
print('%.4f'%R)
print('%.4f'%K)