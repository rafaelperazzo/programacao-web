# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
print('Início')
f=float(input('Digite f: '))
L=float(input('Digite L: '))
Q=float(input('Digite Q: '))
DeltaH=float(input('Digite Delta H: '))
V=float(input('Digite V: '))
G=(9.81)
e=(0.000002)
D=((8*f*L*Q**2)/(G*DeltaH*math.pi**2))**0.2
Rey=(4*Q)/(D*V*math.pi)
K=(0.25)/((math.log10((e/3.7*D)+(5.74/Rey**0.9))**2)
print('%.4f' %D)
print('%.4f' %Rey)
