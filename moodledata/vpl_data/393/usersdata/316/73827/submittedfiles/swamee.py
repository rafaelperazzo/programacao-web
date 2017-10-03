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

