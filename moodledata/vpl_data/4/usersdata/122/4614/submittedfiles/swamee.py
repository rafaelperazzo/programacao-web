# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA

f=input('Digite o valor de f:')
L=input('Digite o valor de L:')
Q=input('Digite o valor de Q:')
H=input('Digite o valor de H:')


#PROCESSAMENTO

D=((8*f*L*(Q**2))/((math.pi**2)*(9.81*H)))**(0.2)

#SAÍDA

print(D)
