# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

f = float(input('Digite o valor de f: ' ))
L = float(input('Digite o valor de L: ' ))
Q = float(input('Digite o valor de Q: ' ))
DeltaH = float(input('Digite o valor de DeltaH: ' ))
v = float(input('Digite o valor de v : '))
g = float(input('Digite o valor de g: ' ))


D = ((8*f*L*Q*Q)/((math.pi**2)*g*DeltaH))**(1/5)


print ('%.4f' %D)


Rey = (4*Q)/(math.pi*D*v)