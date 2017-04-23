# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('Digite o valor:'))
c1=n/20
c2=(n%20)/10
c3=((n%20)%10)/5
c4=(((n%20)%10)%5)/2
c5=((((n%20)%10)%5)%2)/1
print('%d'%c1)
print('%d'%c2)
print('%d'%c3)
print('%d'%c4)
print('%d'%c5)