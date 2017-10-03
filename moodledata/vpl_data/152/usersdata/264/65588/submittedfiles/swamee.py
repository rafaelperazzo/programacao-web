# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f= float(input('Digite o valor de f:'))
l= float(input('Digite o valor de l:'))
q= float(input('Digite o valor de q:'))
deltah= float(input('Digite o valor de deltah:'))
v= float(input('Digite o valor de v:'))
e= 0.00002
g= 9.81
#Processamento:
D= (8*f*l*(q**2)/((math.pi**2)*g*deltah))**(1/5)
Rey= (4*q)/(math.pi*D*v)
k= (0.25)/(math.log10((e/3.7*D)+(Rey**0.9)))**(0.9)
#Saída:
print('%.4f' %D)
print('%.4f' %Rey)
print('%.4f' %k)