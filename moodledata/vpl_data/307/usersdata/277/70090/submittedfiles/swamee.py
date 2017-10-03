# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
# ENTRADAS
f = float(input())
l = float(input())
q = float(input())
dH = float(input())
v = float(input())
# PROCESSAMENTO
pi = math.pi
g = 9.81
e = 0.000002

D = ( (8*f*l*(q**2))/((pi**2)*g*dH) )**(1/5)
print(D)