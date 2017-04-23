# -*- coding: utf-8 -*-
import math
f = float(input('f:'))
L = float(input('L:'))
Q = float(input('Q:'))
DeltaH = float(input('DeltaH:'))
V = float(input('V:'))
g = 9.81
e = 0.000002
pi = math.pi
D = (8*f*L*Q**2/pi**2*g*DeltaH)**0.2
print (D)