# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
F = float(input('digite F : '))
L = float(input('digite L : '))
Q = float(input('digite Q : '))
H = float(input('digite H : '))
V = float(input('digite V : '))
G = 9.81
E = 0.000002
pi=math.pi
D = ((8*F*L*Q*Q)/(pi*pi*G*H))**0.2
REY=(4*Q)/(pi*D*V)
K=0.25/(math.log10(E/3.7*D + 5.74/(REY)**0.9))**2
print('%.4f' %D)
print('%.4f' %REY)
print('%.4f' %K)