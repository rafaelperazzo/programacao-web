# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('Digite o valor:'))
c1=n/20
c2=(n%20)/10
c3=((n%20)%10)/5
c4=(((n%20)%10)%5)/2
c5=((((n%20)%10)%5)%2)/1
print('O numero de cedulas de 20:'%d%c1)
print('O numero de cedulas de 10:'%d%c2)
print('O numero de cedulas de 5:'%d%c3)
print('O numero de cedulas de 2:'%d%c4)
print('O numero de cedulas de 1:'%d%c5)