# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
g = 9.81
E = 0.000002
f = float(input("Digite f:"))
L = float(input("Digite L:"))
Q = float(input("Digite Q:"))
DH = float(input("Digite DH:"))
V = float(input("Digite V:"))
D = (((8*f*L*Q**2)/(math.pi**(2)*g*DH))**0.2)
print("%.4f" % D)
#PROXIMO EXERCICIO
Rey =((4*Q)/(math.pi*D*V))
print("%.4f" % Rey)
#PROXIMO EXERCICIO
k = ((0.25)/(math.log10(E/3.7*D + 5.74/(Rey**0.9))**2))
print("%.4f" % k)