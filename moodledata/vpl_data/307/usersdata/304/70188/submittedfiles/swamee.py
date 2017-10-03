# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f = float(input('Insira f: '))
l = float(input('Insira l: '))
q = float(input('Insira q: '))
dh = float(input('Insira dh: '))
v = float(input('Insira v: '))
g = float(9.81)
e = float(0.000002)
p = float(3.1415)
d = ((8*f*l*(q**2))/(p**2)*g*dh)**(1/5)
rey = (4*q)/(p*d*v)
k = (0.25/(math.log10((e/(3.7*d))+(5.74/(rey**0.9))))**2)
print ('%4.f' %(d))
print ('%4.f' %(rey))
print ('%4.f' %(k))
