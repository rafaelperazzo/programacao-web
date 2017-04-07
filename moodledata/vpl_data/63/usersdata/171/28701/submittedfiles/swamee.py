# -*- coding: utf-8 -*-
import math
g=9.81
e=0.000002
pi=math.pi
f=float(input('digite f:))
l=float(input('digite l:))
q=float(input('digite q:))
deltah=float(input('digite delta h :'))
d=((8*f*l*q**2)/(pi**2)*deltah))**0.5
print('%.4f'%d)