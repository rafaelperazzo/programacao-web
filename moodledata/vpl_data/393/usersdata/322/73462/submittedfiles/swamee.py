# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
#ENTRADA

f= float(input(' digitar valor para f: '))
L= float(input(' digitar valor para L: '))
Q= float(input(' digitar valor para Q: '))
DeltaH= float(input(' digitar valor para DeltaH: '))
v= float(input(' digitar valor para v: '))

#PROCESSAMENTO

D= ((8*f*L*Q**2)/((math.pi**2)*9.81*DeltaH))**(1/5.0)
Rey= (4*Q)/(math.pi*D*v)
K= (0.25)/math.log10((0.000002/3.7*D)+(5.74/Rey**0.9))**2

#SAIDA
print('%.4f'%D)
print('%.4f'%Rey)
print('%.4f'%K)
