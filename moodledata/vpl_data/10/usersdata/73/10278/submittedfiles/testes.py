# -*- coding: utf-8 -*-
from __future__ import division
n=input('digite o valor de 3 algarismos que voce deseja inverter:')
a=n//100
b=(n%100)//10
c=(n%100)%10
d= c*100+b*10+a
print d