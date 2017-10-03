# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
g = 9.81
print("g =", g)
e = 0.000001
print("e =", e)
pi = math.pi
print("pi = ", pi)
f = float(input("f? :"))
L = float(input("L? :"))
Q = float(input("Q? :"))
DeltaH = float(input("DeltaH? :"))
v = float(input("v? :"))
D = ((8*f*L*(Q**2))/((math.pi**2)*g*DeltaH))**0.2
print("D = ", D)
Rey = (4*Q)/(pi*D*v)
print("Rey = ", Rey)
k = 0.25/((math.log10)*((e/(3.7)*D)+((5.74)/Rey**0.9))**2
print("k = ", k) 