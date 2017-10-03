# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f= float(input('Digite o valor de f:'))
L= float(input('Digite o valor de L:'))
Q= float(input('Digite o valor de Q:'))
DELTAH= float(input('Digite o valor de DELTAH:'))
v= float(input('Digite o valor de v:'))

g= 9.81
E= 0.000002

D= ((8*f*L*Q*Q)/(math.pi*math.pi*g*DELTAH))**(1/5)
Rey= (4*Q)/(math.pi*D*v)
k= (0.25)/(