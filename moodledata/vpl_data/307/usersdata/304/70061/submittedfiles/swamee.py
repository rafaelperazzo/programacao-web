# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f = float(input('Insira f: '))
l = float(input('Insira l: '))
q = float(input('Insira q: '))
dh = float(input('Insira dh: '))
v = float(input('Insira v: '))
g = 9.81
e = 0.000002
p = math.pi
d = ((8*f*l*(q**2))/(p**2)*g*dh)**(1/5)
print (float(d))
