# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('Digite o valor de n:'))
v1=n/20
v2=(n%20)/10
v3=((n%20)%10)/5
v4=(((n%20)%10)%5)/2
v5=((((n%20)%10)%5)%2)/1
print('%d'%v1)
print('%d'%v2)
print('%d'%v3)
print('%d'%v4)
print('%d'%v5)