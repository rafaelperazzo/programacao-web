# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

#COSTANTES
g=9.81
E=0.000002

f =float(input('Digite valo para f: '))
L =float(input('Digite valo para L: '))
Q =float(input('Digite valo para Q: '))
dH=float(input('Digite valo para dH: '))
v =float(input('Digite valo para v: '))

D = (((8*f*L*(Q**2))/(((math.pi)**2)*g*dH))**0.2)

Rey = ((4*Q)/(math.pi)*D*v)

a= (E/(3.7*D))
b= (5.74/(Rey**0.9))

k = (0.25/(math.log10(a+b))**2)

print('Valor de D: ' '%.4f' %D)
print('Valor de Rey: ' '%.4f' %Rey)
print('Valor de k: ' '%.4f' %k)