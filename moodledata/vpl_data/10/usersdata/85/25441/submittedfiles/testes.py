# -*- coding: utf-8 -*-
from __future__ import division

n= input('Digite o valor de n: ')

a= n%10
b= (n//10)%10
c= (((n//10)//10)%10)
d= ((((n//10)//10)//10)%10)

print d
print c
print b
print a