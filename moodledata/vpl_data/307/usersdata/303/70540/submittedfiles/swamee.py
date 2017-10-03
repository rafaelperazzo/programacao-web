# -*- coding: utf-8 -*-
import math
f= float(input('Digite f:'))
L= float(input('Digite L:'))
Q= float(input('Digite Q:'))
Deltah= float(input('Digite Delta h:'))
g= 9.81
e= 0.000002
numerador=float(8*f*L*(Q**2))
denominador=float((math.pi**2)*g*Deltah)
D=float(((numerador/denominador)**0.2))
print('%.4f'%D)
v=float(input('Digite v:'))
Rey=((4*Q)/(math.pi*D*v))
print('%.4f'%Rey)
k=((0.25)/((math.log10((e/(3.7*D))+((5.74)/(Rey**0.9))))**2)
print('%.4f'%k)