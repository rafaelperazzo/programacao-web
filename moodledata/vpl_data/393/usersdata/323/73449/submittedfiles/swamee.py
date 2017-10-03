# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f = float (input ('f: '))
L = float (input ('L: '))
Q = float (input ('Q '))
DeltaH = float (input ('DeltaH: '))
v = float (input ('v: '))

g = 9.81
e = 0.000002

D = ((8*f*L*Q*Q)/(math.pi*math.pi*g*DeltaH))**(0.2)
Rey = (4*Q)/(math.pi*D*v)
dentrolog = (e/(3.7*D)) + (5.74/(Rey**0.9))
k = 0.25/ ((math.log10(dentrolog))**2)

print ('%.4f' %D)
print ('%.4f' %Rey)
print ('%.4f' %k)
