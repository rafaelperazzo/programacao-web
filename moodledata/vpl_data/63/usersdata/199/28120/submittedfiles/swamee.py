# -*- coding: utf-8 -*-
import math
Efe = float(input('Digite o valor de Efe: '))
L = float(input('Digite o valor de L: '))
Q = float(input('Digite o valor de Q: '))
DeltaH = float (input('Digite o valor de DeltaH: '))
v = float (input('Digite o valor de v: '))
g = float(input('Digite o valor de g: '))
e = float (input('Digite o valor de e: '))
Pi = float (input('Digite o valor de Pi: '))
D = (8*Efe*L*Q*Q) / (Pi*g*DeltaH)
D1 = (D*D*D*D*D)
print ('%2f' % D1 )