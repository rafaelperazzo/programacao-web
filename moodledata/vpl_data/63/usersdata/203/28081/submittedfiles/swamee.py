# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
pi=math.pi
g=9.81
E=0.000002
f=float(input('Digite f:'))
L=float(input('Digite L:'))
Q=float(input('Digite Q:'))
deltaH=float(input('Digite deltaH:'))
v=float(input('Digite v:'))
D=((8*f*L*Q*Q)**(1/5))/((pi*pi*g*deltaH)**(1/5))
print(D)