# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

g=9.81
e=0.000002
f=float(input("digite o valor de f:"))
L=float(input("digite o valor de L:"))
Q=float(input("digite o valor de Q:"))
deltah=float(input("digite o valor de deltah:"))
v=float(input("digite o valor de v:"))
D=((8*f*L*(Q**2))/((math.pi**2)*g*deltah))**(0.2)
print(D)
