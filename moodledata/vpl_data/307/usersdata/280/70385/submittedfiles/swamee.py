# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input("f= "))
l=float(input("l= "))
q=float(input("q= "))
deltaH=float(input("Delta H= "))
v=float(input("v= "))
g=float(9.81)
e=float(0.000002)
d=float(((8*f*l*(q**2))/(((math.pi)**2)*g*deltaH))**0.2)
rey=float((4.0*q)/((math.pi)*d*v))
a=float(e/3.7*d)
b=float(5.74/(rey**0.9))
c=float((math.log10(a+b))**2.0)
k=float(0.25/c)
print (float("%.4f" %(d)))
print (float("%.4f" %(rey)))
print (float("%.4f" %(k)))