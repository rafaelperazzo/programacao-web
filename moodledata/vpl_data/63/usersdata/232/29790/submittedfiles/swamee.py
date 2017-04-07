# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('Digite o valor de f: '))
L=float(input('Digite o valor de L: '))
Q=float(input('Digite o valor de Q: '))
H=float(input('Digite o valor de DeltaH: '))
v=float(input('Digite o valor de v: '))
g=9.81
e=0.000002
pi=math.pi
D=(8*f*L*(Q**2))/((pi**2)*g*H))**(0.2)
print('%f' %D)