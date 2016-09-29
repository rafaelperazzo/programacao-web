# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f=input("Digite o valor de f:")
L=input("Digite o valor de L:")
Q=input("Digite o valor de Q:")
DH=input("Digite o valor de DH:")
v=input("Digite o valor de v:")
z=8
g=9.81
e=0.000002
D=(z*f*L*(Q**2))/((math.pi**2)*g*DH)**1/5
Rey=(4*Q)/(math.pi*D*v)
k=0.25/(math.log10(e/(3.7*D)+(5.74/(Rey**0.9))))**2
print("D= %.4f" %(D))
print("Rey= %.4f" %(Rey))
print("k= %.4f" %(k))