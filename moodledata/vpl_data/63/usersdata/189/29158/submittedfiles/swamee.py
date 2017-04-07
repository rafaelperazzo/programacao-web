# -*- coding: utf-8 -*-
import math
f= float(input('digite f:'))
l= float(input('digite l:'))
q= float(input('digite q:'))
delta= float(input('digite delta:'))
v= float(input('digite v:'))
D=(8*f*l*q**2/math.pi**2*9.81*delta)**0.2
rey=(4*q/math.pi*D*v)
k=0.25/(math.log10((0.000002/3.7*D)+(5.74/rey**0.9)))**2
print('%.4f %D)
print('%.4f %rey)
print('%.4f %k)