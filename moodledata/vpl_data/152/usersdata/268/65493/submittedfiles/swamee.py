# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

f= float(input('Digite o valor de f: '))
L= float(input('Digite o valor de L: '))
Q= float(input('Digite o valor de Q: '))
DeltaH= float(input('Digite o valor de DeltaH: '))
v= float(input('Digite o valor de v: '))
g=9,81
E=0.000002

D= ((8*f*L*Q*Q)/((math.pi**2)*g* DeltaH ))**(1/5)

Rey= (4*Q)/((math.pi)*D*v)

a= E/(3.7*D)
b= 5.74/((Rey)**0.9)

k= 0.25/((math.log10(a+b))**2)

print(D)
print(Rey)
print(k)
