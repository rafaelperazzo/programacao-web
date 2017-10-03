# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
F=float(input('digite F : '))
L=float(input('digite L : '))
Q=float(input('digite Q : '))
H=float(input('digite H : '))
V=float(input('digite V : '))
G=9,81
E=0,000002
D=((8*F*L*(Q**2))/(((math.pi)**2)*G*H))**0.2
REY=(4*Q)/(math.pi*d*v)
k=(0.25)/(math.log10((E)/(3.7*D)+(5.74)/(REY**0.9)))
print('%.4f' %D)
print('%.4f' %REY)
print('%.4f' %K)