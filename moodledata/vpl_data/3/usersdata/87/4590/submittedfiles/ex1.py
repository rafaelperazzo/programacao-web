# -*- coding: utf-8 -*-
from __future__ import division

#COMECE A PARTIR DAQUI!

a = input("Digite valor de a:")
b = input("Digite valor de b:")
c = input("Digite valor de c:")

Delta = (b**2(-4*a*c))**0.5
x1 = (-b + Delta)/2*a
x2 = (-b - Delta)/2*a

if Delta>=0:
    print("valor de x1: %.1f" %x1)
    print("valor de x2: %.1f" %x2)
else:
    print("SRR")
