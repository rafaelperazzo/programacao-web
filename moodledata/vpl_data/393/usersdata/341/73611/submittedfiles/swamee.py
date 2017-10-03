# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f = float(input('Digite o valor de f: '))
L = float(input('Digite o valor de L: '))
Q = float(input('Digite o valor de Q: '))
DeltaH = float(input('Digite o valor de DeltaH: '))
v = float(input('Digite o valor de v: '))
g = 9.81
e = 0.000002
#PROCESSAMENTO
D = ((8*f*L*Q*Q)/(math.pi*math.pi*g*DeltaH))**(0.2)
#CÁLCULO DO Rey
Rey = (4*Q)/(math.pi*D*v)
#CÁLCULO DO k
k = (0.25)/((math.log10((e)/(3.7*D) + (5.74)/(Rey**0.9)))**2)
#SAÍDA
print('valor de D: %.4f' %D)
print('valor de Rey: %.4f' %Rey)
print('valor de k: %.4f' %k)

