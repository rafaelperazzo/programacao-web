# -*- coding: utf-8 -*-
import math
f= float(input('digite f:'))
l= float(input('digite l:'))
q= float(input('digite q:'))
delta= float(input('digite delta:'))
v= float(input('digite v:'))
d=(8*f*l*(q*q)/3.14159**2*9.81*delta)
rey=((4*q)/(3.14159*d*v))
k=0.25/(math.log10(0.000002/3.7*d+5.74/rey**0.9))**2
print('O valor de D é %.4f' %d)
print('O valor de Rey é %.4f' %rey)
print('O valor de K é %.4f' %k)