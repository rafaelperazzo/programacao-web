# -*- coding: utf-8 -*-
import math
f = 0.2
L = 5000
Q = 0.65
DeltaH = 22
v = 0.000001
g = float(input('Digite o valor de g: '))
e = float (input('Digite o valor de e: '))
Pi = float (input('Digite o valor de Pi: '))
D = (8*Efe*L*Q*Q) / (Pi*g*DeltaH)
D1 = (D*D*D*D*D)
print ('%2f' % D1 )