# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
g = float(9.81)
epsilon = float(0.000002)
pi = float(math.pi)

f = float(input('Digite f: '))
L = float(input('Digite L: '))
Q = float(input('Digite Q: '))
DeltaH = float(input('Digite DeltaH: '))
v = float(input('Digite v: '))

D = float((((8*f*L*(Q**2))/((pi**2)*g*DeltaH))**(0.2)))

Rey = float((4*Q)/(pi*D*v))

k = float((0.25)/((math.log10((epsilon/(3.7*D))+(5.74/(Rey**0.9))))**2))

print('\n')
print('%.4f' % D)
print('%.4f' % Rey)
print('%.4f' % k)