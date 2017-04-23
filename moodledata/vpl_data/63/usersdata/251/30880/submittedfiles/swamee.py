# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f = float (input('Insira o valor f: '))
l = float (input('Insira o valor l: '))
q = float (input('Insira o valor q: '))
deltaH = float (input('Insira o valor Delta H: '))
v = float (input('Insira o valor v: '))

g = 9.81
e = 0.000002

D = ( ((8*f*l*(q*q))/((math.pi**2)*g*deltaH))**(1/5) )

Rey = ((4*q)/(math.pi*D*v))

x = (e/(3.7*D))
y = (5.74/(Rey**0.9))
k = (0.25/(math.log10(x+y))**2)

print('%4.f'%D)
print('%4.f'%Rey)
print('%4.f'%k)
