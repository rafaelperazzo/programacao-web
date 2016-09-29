# -*- coding: utf-8 -*-
from __future__ import division
print('Programa para verificar se uma gangorra está ou não em equilíbro.')
print('Na condição de equilíbro o torque resultante é nulo. Assim, P1*C1=P2*c2')
p1=input('Digite o valor de p1')
c1=input('Digite o valor de c1')
p2=input('Digite o valor de p2')
c2=input('Digite o valor de c2')
if(p1*c1==p2*c2):
    print('0')
elif(p1*c1>p2*c2):
    print('-1')
else:
    print('1')