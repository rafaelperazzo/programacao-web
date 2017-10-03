# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
# ENTRADAS
f = float(input())
l = float(input())
q = float(input())
dH = float(input())
v = float(input())
# PROCESSAMENTO
pi = math.pi
g = 9.81
e = 0.000002

D = ( (8.0*f*l*(q**2.0))/((pi**2.0)*g*dH) )**(1.0/5.0)
print("%.4f" % D)
Rey = ( (4.0*q) / (pi*D*v) )
print("%.4f" % Rey)
k = 0.25 / ( (math.log10( (e/(3.7*D)) + ((5.74)/(Rey**0.9)) ))**2.0 )
print("%.4f" % k)