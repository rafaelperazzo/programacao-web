# -*- coding: utf-8 -*-
import math
g=9.81
E=0.000002
f=float(input('digite f:'))
L=float(input('digite L:'))
Q=float(input('digite Q:'))
deltaH=float(input('digite deltaH:'))
v=float(input('digite v:'))
D=((8*f*L*(Q**2))/((math.pi**2)*g*deltaH))*0.2
print('%.4f' %D)
Rey=(4*D)/((math.pi)*D*v)
print('%.4f' %Rey)
k=(0.25)/(math.log10(((E/(3.7*D))+(5.74/(rey**0.9)))*math.log10(((E/(3.7*D))+(5.74/(rey**0.9))))
print(k)