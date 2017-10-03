# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input("digite um valor de f: "))
L=float(input("digite um valor de L: "))
Q=float(input("digite um valor de Q : "))
DeltaH=float(input("digite um valor de VH: "))
v=float(input("digite um valor de de v: "))
g=9.81
e=0.000002
D=(((8*f*L*Q**2)/(math.pi**(2)*g*(DeltaH)))**0.2)
Rey=(4*Q)/(math.pi*D*v)
K=((0.25)/((math.log10((e/(3.7)*D)+(5.74/(Rey**(0.9)))))**2))
print(%.4d %D)
print(%.4d %Rey)
print(%.4d %K)







