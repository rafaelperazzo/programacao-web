# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

#calcular o D 

f = float(input('digite f: '))
L = float(input('digite L: ')) 
Q = float(input('digite Q: ')) 
deltaH = float(input('digite deltaH: ')) 
v = float(input('digite v: '))
g = 9.81
e = 0.000002

D = (((8*f*L*(Q**2))/((math.pi**2)*g*deltaH))**0.2)

#calcular o Rey

Rey = ((4*Q)/(math.pi*D*v))


#calcular K

k = ((0.25)/((math.log10(((e)/(307*D)) + ((5.74)/(Rey**0.9))))**2))
print ('%.4f' %k)













