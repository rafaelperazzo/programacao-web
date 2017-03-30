# -*- coding: utf-8 -*-
import math
f = 0.2
L = 50000
Q = 0.65
DeltaH = 22
v = 0.000001
g = float(input('Digite o valor de g: '))
e = float (input('Digite o valor de e: '))
Pi = float (input('Digite o valor de Pi: '))
D = (8*f*L*Q*Q) / (Pi*Pi*g*DeltaH) * (8*f*L*Q*Q) / (Pi*Pi*g*DeltaH) * (8*f*L*Q*Q) / (Pi*Pi*g*DeltaH) * (8*f*L*Q*Q) / (Pi*Pi*g*DeltaH) *(8*f*L*Q*Q) / (Pi*Pi*g*DeltaH)
print ('%4f' % D )