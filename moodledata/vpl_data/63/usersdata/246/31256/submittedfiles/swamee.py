# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
F = float(input('Digite o valor de F: '))
L = float(input('Digite o valor de L: '))
Q = float(input('Digite o valor de F: '))
DH = float(input('Digite o valor de Delta H: '))
V = float(input('Digite o valor de V: '))
G = 9.81
E = 0.000002
D = ((8*F*L*Q**2)/(math.pi**2*G*DH))**0.2
K = (0.25) ((math.log10(E/(3.7*D))*((5.74)/REY**0.9)))**0.2
REY = (4*Q)/(math.pi*D*V)
print('%4F'%D)
print('%4F'%REY)
print('%4F'%K)
