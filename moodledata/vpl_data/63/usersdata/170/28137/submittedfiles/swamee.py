# -*- coding: utf-8 -*-
import math
f=float(input('Digite o valor de f:'))
L=float(input('Digite o valor de L:'))
Q=float(input('Digite o valor de Q:'))
DeltaH=float(input('Digite o valor de DeltaH:'))
v=float(input('Digite o valor de v:'))
g=9.81
e=0.000002
math.pi=3.14159
D=((8*f*L*Q*Q)/(math.pi*math.pi*g*DeltaH))**1/5
Rey=(4*Q)/(math.pi*D*v)
k=0.25/()**2