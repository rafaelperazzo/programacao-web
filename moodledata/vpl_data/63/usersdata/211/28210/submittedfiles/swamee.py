# -*- coding: utf-8 -*-
import math
f=float(input('digite f:'))
l=float(input('digite l:'))
q=float(input('digite q:'))
deltaH=float(input('digite deltaH'))
v=float(input('digite v'))
g=9.81
e=0.000002
D=((8*f*l*q**2)/(math.pi**2*g*deltaH))**0.2
Rey=(4*q)/(math.pi*D*v)
