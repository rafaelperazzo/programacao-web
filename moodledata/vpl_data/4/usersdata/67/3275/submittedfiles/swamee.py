# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f=input("Digite o valor de f:")
L=input("Digite o valor de L:")
Q=input("Digite o valor de Q:")
DH=input("Digite o valor de DH:")
v=input("Digite o valor de v:")
g=9.81
e=0.000002
D1=(8*f*L*(Q**2))
D2=(math.pi**2)*g*DH
D=(D1/D2)**0.2
Rey=((4*Q)/((math.pi)*D*v))
k1=e/(3.7*D)
k2=5.74/(Rey)**0.9
k=(0.25)/(math.log10((k1)+(k2)))**2
print("D= %.4f" %(D))
print("Rey= %.4f" %(Rey))
print("k= %.4f" %(k))