# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

f= int(input('digite o valor de f:'))

L= int(input('digite o valor de L:'))

Q= int(input('digite o valor de Q:'))

DeltaH= int(input('digite o valor de DeltaH:'))

v= int(input('digite o valor de v:'))

g=9.81

E=0.000002

math.pi=3.141592

D=((8*f*L*Q**2)/((math.pi**2)*g*DeltaH))**-5


