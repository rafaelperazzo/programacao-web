# -*- coding: utf-8 -*-
import math
f =float (input('Digite o valor de f:'))
L =float (input('Digite o valor de L:'))
Q =float (input('Digite o valor de Q:'))
DeltaH = float (input('Digite o valor de DeltaH:'))
v =float (input('Digite o valor de v:'))
g = float (input('Digite o valor de g:'))
e = float (input('Digite o valor de e:'))
D1 = ((8*f*L*Q**2)/(math.pi**2*g*DeltaH))
D =(D1*D1*D1*D1)
Rey = (4*Q) / (math.pi*D*v)
k = (0.25) /((math.log10(e/3.7*D))*(5.74/Rey**0.9))**2
print ('%4f' % D )
print ('%4f' % Rey)
print ('%4f' % k) 