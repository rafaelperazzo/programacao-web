# -*- coding: utf-8 -*-
import math 
f=float(input('digite f:'))
l=float(input('digite l:'))
q=float(input('digite q:'))
deltaH=float(input('digite detalH:'))
v=float(input('digite v:'))
g=(9.81)
e=(0.000002)

d=((8*f*l*(q**2))/((math.pi**2)*g*deltaH))**0.2
rey=(4*q)/(math.pi*d*v)
k=0.25/(math.log10((e/(3.7*d))+(5.74)/(rey**0.9)))**2

print('%.4f'%d)
print('%.4f'%rey)
print('%.4f'%k)