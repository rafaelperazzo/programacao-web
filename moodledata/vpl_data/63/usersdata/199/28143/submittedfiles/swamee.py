# -*- coding: utf-8 -*-
import math
f = 0.2
L = 50000
Q = 0.65
DeltaH = 22
v = 0.000001
D1 = ((8*f*L*Q**2 / math.pi**2*9.81*DeltaH))
D = (D1*D1*D1*D1)
print ('%4f' % D )
Rey = (4*Q) / (math.pi*D*v)
print ('%4f' % Rey)