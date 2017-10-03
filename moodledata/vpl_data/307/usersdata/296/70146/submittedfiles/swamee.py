# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
g = 9.81
E = 0.000002
f = float(input("Digite o valor de f: "))
L = float(input("Digite o valor de L: "))
Q = float(input("Digite o valor de Q: "))
DH = float(input("Digite o valor de D: "))
V = float(input("Digite o valor de V: "))
D = ((8*f*L*(Q**2)/(math.pi**2)*g*DH)**1/5)
print(D)
