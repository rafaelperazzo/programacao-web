# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f= float(input('Digite f: '))
L= float(input('Digite L: '))
Q= float(input('Digite Q: '))
DeltaH= float(input('Digite DeltaH: '))
v= float(input('Digite v: '))
g=9.81
E=0.000002
D=(((8*f*L*Q**2)/((math.pi)**2*g*DeltaH))**0.2)
Rey=((4*Q)/((math.pi)*D*v))
print('%.4f' %D)
print('%.4f' %Rey)