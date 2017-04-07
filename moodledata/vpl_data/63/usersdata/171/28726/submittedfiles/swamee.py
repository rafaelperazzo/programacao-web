# -*- coding: utf-8 -*-
import math
g=9.81
e=0.000002
pi=math.pi
f=float(input('digite f:'))
l=float(input('digite l:'))
q=float(input('digite q:'))
v=float(input('digite v:'))
deltah=float(input('digite delta h :'))
d=(8*f*l*(q*q))**0.2/((math.pi*math.pi)*g*deltah)**0.2
rey=(4*q)/(math.pi*d*v)
k=0.25/math.log10(e/3.7*d*)+(5.74/rey**0.9)**2
print('%.4f%d')
print('%.4f%rey')
print('%.4f%k')