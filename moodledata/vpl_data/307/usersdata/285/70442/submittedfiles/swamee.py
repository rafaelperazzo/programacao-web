# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
g = 9.81
E = 0.000002
f = float(input("digite o valor de f: "))
L = float(input("digite o valor de L: "))
Q = float(input("digite o valor de Q: "))
DH = float(input("digite o valor de DH: "))
V = float(input("digite o valor de V: "))
D = (((8*f*L*Q**2)/(math.pi**(2)*g*DH))**0.2)
print("%.4f" % D)
#PROXIMA FÓRMULA
Rey = ((4*Q)/(math.pi*D*V))
print("%.4f" % (Rey))
#PROXIMA FÓRMULA
K =((0.25)/(math.log10(((E)/(3.7*D))+((5.74)/(Rey**0.9))))**2) 