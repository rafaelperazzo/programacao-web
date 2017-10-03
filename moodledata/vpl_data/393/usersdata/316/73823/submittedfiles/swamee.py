# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

g=9,81
e=0,000002
f=float(input("digite o valor de f:"))
L=float(input("digite o valor de L:"))
Q=float(input("digite o valor de Q:"))
deltah=float(input("digite o valor de deltah:"))
v=float(input("digite o valor de v:"))
D=(1/5)**((8*f*L*Q*Q)/(math.pi*math.pi*g*deltah))
print(D)
Rey=(4*q)/(math.pi*D*v)
k=(1/4)*(1/math.log10((e/3,70)+((5,74/(Rey**(9/10)))))