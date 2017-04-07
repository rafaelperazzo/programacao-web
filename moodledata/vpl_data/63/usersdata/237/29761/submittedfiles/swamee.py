# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input("digite f:"))
l=float(input("digite l:"))
q=float(input("digite q:"))
h=float(input("digite h:"))
v=float(input("digite o:"))
g=9.81
e=0.000002
D= ((8*f*l*(q*q))/((math.pi**2)*g*h))**(1/5)
Rey=(4*q)/(math.pi*D*v)
k=0.25/((math.log10((e/3.7*D)+(5.74/(Rey**(0.9)))**2)
print("%.4f" % (D))
print("%.4f" % (Rey))
print("%.4f" % (k))