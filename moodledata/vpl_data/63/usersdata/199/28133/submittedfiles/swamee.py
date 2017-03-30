# -*- coding: utf-8 -*-
import math
f = 0.2
L = 50000
Q = 0.65
DeltaH = 22
v = 0.000001
g = float(input('Digite o valor de g: '))
e = float (input('Digite o valor de e: '))
Pi = math.pi 
D1 = (8*f*L*Q*Q) / (Pi*Pi*g*DeltaH) 
D = (D1*D1*D1*D1*D1)
print ('%4f' % D )
Rey = (4*Q) / (Pi*D*v)
print ('%4f' % Rey)