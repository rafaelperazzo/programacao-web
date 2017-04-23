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
D = ((8*f*L*Q**2)/(pi**2*g*DeltaH))**0.2
Rey = 4*Q/pi*D*V
k = (0.25)/(math.log10((e/3.7*D)+(5.74/Rey**0.9)))**2
print ('%4f' %D)
print ('%.4f' %Rey)
print ('%.4f' %k)