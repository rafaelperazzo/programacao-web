# -*- coding: utf-8 -*-
import math
f= float(input('Digite f:'))
L= float(input('Digite L:'))
Q= float(input('Digite Q:'))
Deltah= float(input('Digite Delta h:'))
g= 9.81
e= 0.000002
numerador=(8*f*L*(Q**2))
denominador=((math.pi**2)*g*Deltah)
D=((numerador/denominador)**0,2)
print('%4f' %D)
