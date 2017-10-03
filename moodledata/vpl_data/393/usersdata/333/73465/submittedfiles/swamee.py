# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f = float(input("f? :"))
L = float(input("L? :"))
Q = float(input("Q? :"))
DeltaH = float(input("DeltaH? :"))
v = float(input("v? :"))
g = input(9.81)
e = input(0.000001)
pi = math.pi
D = ((8*f*L*(Q**2))/((pi**2)*g*DeltaH))**0.2