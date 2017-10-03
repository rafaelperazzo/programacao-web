# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

#ENTRADA
f= 0.2
L= 50000
Q= 0.65
DeltaH= 22
v= 0.000001

#PROCESSAMENTO
t= float(1/5)
D= ((8*f*L*Q**2)/(math.pi**2*9.81*DeltaH))**t
Rey= (4*Q)/(math.pi*D*v)
k= (0.25)/((math.log10(((0.000002)/(3.7*D))+((5.74)/(Rey**0.9)))**2))

#SAÍDA
print('%.4f' % D)
print('%.4f' % Rey)
print('%.4f' % k)
print(t)