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
R*e*y = (4*Q)/(pi*D*v)
print("R*e*y = ", R*e*y)