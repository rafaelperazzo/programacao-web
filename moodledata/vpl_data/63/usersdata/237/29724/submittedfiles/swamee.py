# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input("digite f:"))
l=float(input("digite l:"))
q=float(input("digite q:"))
h=float(input("digite h:"))
o=float(input("digite o:"))
g=9.81
e=0.000002
D= ((8*f*l*(q*q))/((math.pi**2)*g*h))**(1/5)
Rey=(4*q)/(math.pi*D*o)
Print("%f , %f" % (D, Rey))