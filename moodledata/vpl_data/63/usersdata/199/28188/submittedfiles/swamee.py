# -*- coding: utf-8 -*-
import math
f =float (input('Digite o valor de f'))
L =50000
Q =0.65
DeltaH = 22
v =0.000001
e=0.000002
D = ((8*f*L*Q**2)/(math.pi**2*9.81*DeltaH))*0.2
Rey = (4*Q) / (math.pi*D*v)
k = (0.25) /((math.log10(e/3.7*D))*(5.74/Rey**0.9))**2
print ('%4f' % D )
print ('%4f' % Rey)
print ('%4f' % k) 