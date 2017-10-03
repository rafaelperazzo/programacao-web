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
D =((8*f*L*(Q**2)/(math.pi**2)*g*DH)**1/5)
print("&.4f" % (D))