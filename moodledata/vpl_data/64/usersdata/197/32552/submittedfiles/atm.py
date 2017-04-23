# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
saque=int(input('Digite o valor a ser sacado:'))
a=saque//20
b=saque%20
c=b//10
d=c%10
e=d//5
f=e%5
g=f//2
h=g//1
print('Numero de cedulas de 20 igual a:%d'%a)
print('Numero de cedulas de 10 igual a:%d'%c)
print('Numero de cedulas de 5 igual a:%d'%e)
print('Numero de cedulas de 2 igual a:%d'%g)
print('Numero de cedulas de 1 igual a:%d'%h)