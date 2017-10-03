# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input("f= "))
l=float(input("l= "))
q=float(input("q= "))
deltaH=float(input("Delta H= "))
v=float(input("v= "))
g=9.81
e=0.000002
d=((8*f*l*(q**2))/(((math.pi)**2)*g*deltaH))**0.2
rey=(4*q)/((math.pi)*d*v)
a=e/3.7*d
b=5.74/(rey**0.9)
c=(math.log10(a+b))**2
k=0.25/c
print ("%.4f" %(d))
print ("%.4f" %(rey))
print ("%.4f" %(k))