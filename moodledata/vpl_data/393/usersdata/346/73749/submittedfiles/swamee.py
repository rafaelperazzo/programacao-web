# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

#ENTRADA
f= float(input('Digite um valor para f: '))
L= float(input('Digite um valor para L: '))
Q= float(input('Digite um valor para Q: '))
DeltaH= float(input('Digite um valor para DeltaH: '))
v= float(input('Digite um valor para v: '))
g= 9,81
libra= 0,000002
pi= (math.pi)

#PROCESSAMENTO
D= ((8*f*L*Q**2)/((pi**2)*g*DeltaH))**(1/5)
Rey= (4*Q)/(pi*D*v)
k= (0,25)/((match.log10(((libra)/(3.*D))+((5.74)/(Rey**0.9)))**2)

#SAÍDA

print('%.4f' % Rey)
print('%.4f' % k)