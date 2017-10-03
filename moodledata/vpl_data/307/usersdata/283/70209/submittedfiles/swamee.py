# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input("Determine f: "))
L=float(input("Determine L: "))
Q=float(input("Determine Q: "))
dH=float(input("Determine dH: "))
v=float(input("Determine v: "))

pi=3.1415
g=9.81
e=0.000002

D=((8*f*L*Q**2)/(pi**2*g*dH))**1/5

print('D = D')