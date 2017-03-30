# -*- coding: utf-8 -*-
import math
f =0.2
L =50000
Q =0.65
DeltaH = 22
v =0.000001
g =9.81
e = 0.000002
D = (8*f*L*Q**2) / (math.pi**2*9.81*DeltaH)*0.2
Rey = (4*Q) / (math.pi*D*v)
print ('%4f' % D )
print ('%4f' % Rey)