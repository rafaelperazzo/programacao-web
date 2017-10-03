# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f = float(input('digite um valor qualquer; '))
l = float(input('digite um valor qualquer: '))
q = float(input('digite um valor qualquer; '))
deltaH = float(input('digite um valor qualquer; '))
v = float(input('digite um valor qualquer; '))
g = 9.81
epsilon = 0.000002
d = ((8*f*l*(q)**2)/((math.pi)**2*g*deltaH))**(0.2)
print('%.4f' %d)
rey = ((4*q)/(math.pi*d*v))
print('%.4f' %rey)
k = (0.25)/(math.log10(((epsilon)/(3.7*d))+((5.74)/(rey**0.9))))**2
print('%.4f' %k)