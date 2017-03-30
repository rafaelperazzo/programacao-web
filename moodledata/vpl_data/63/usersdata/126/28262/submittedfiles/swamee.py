# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

f= float(input('digite o valor de f:'))

L= float(input('digite o valor de L:'))

Q= float(input('digite o valor de Q:'))

DeltaH= float(input('digite o valor de DeltaH:'))

v= float(input('digite o valor de v:'))

g=9.81

E=0.000002

math.pi=3.141592

D=((8*f*L*Q**2)/((math.pi**2)*g*DeltaH))**-5

Rey= (4*Q)/(math.pi*D*v)




