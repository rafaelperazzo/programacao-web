# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

f=float(input('Digite f:'))
l=float(input('Digite l:'))
q=float(input('Digite q:'))
deltaH=float(input('Digite deltaH:'))
v=float(input('Digite v:'))

g=9.81
E=0.000002

D=((8*f*l*q**2)/(math.pi**2*g*deltaH)) **0.2

Rey=(4*q)/(math.pi*D*v)

K=(0.25)/((math.log10((E/3.7*D)*(5.74/Rey**0.9))))**2
print('%.4f' %D)
print('%.4f' %Rey)
print('%.4f' %K)

