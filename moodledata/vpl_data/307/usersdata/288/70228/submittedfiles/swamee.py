# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
print("Olá, vamos calcular o valor de K")
f=float(input("digite um valor de f: "))
L=float(input("digite um valor de L: "))
Q=float(input("digite um valor de Q : "))
DeltaH=float(input("digite um valor de VH: "))
v=float(input("digite um valor de de v: "))
g=9.81
e=0.000002
D=(((8*f*L*Q**2)/(math.pi**(2)*g*(DeltaH)))**0.2)
Rey=(4*Q)/(math.pi*D*v)
print("%.4d" %D)
