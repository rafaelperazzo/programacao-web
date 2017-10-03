# -*- coding: utf-8 -*-
import math
#ENTRADA
f = float(input('Digite o valor de f: '))
L = float(input('Digite o valor de L: '))
Q = float(input('Digite o valor de Q: '))
H = float(input('Digite o valor de H: '))
v = float(input('Digite o valor de v: '))
#PROCESSAMENTO
D = (((8*f*L*(Q*Q))/((math.pi)*(math*pi)*9.81*H))**(1/5))
Rey = (4*Q)/((math.pi)*D*v)
j = ((0.000002)/((3.7)*D))+((5.74)/((rey)**(0.9)))
K = (o.25)/((math.log(j))**2)

print('O valor do diâmetro