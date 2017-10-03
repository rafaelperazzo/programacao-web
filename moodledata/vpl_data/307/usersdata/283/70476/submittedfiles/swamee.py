# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input("Determine f: "))
L=float(input("Determine L: "))
Q=float(input("Determine Q: "))
dH=float(input("Determine dH: "))
v=float(input("Determine v: "))

pi=math.pi
g=9.81
e=0.000002

D=((8*f*L*(Q**2))/((pi**2)*g*dH))**0.2

Rey=(4*Q)/(pi*D*v)

k=((0.25)/(math.log10(((e)/(3.7*D))*(5.74)/(Rey)**9/10)))**2
print(' %.4f' % D)
print(' %.4f' % Rey)
print(' %.4f' % k)