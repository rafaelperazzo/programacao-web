# -*- coding: utf-8 -*-
from __future__ import division

n= input('Digite o valor de n: ')

a= n%10
b= (n//10)%10
c= (((n//10)//10)%10)
d= ((((n//10)//10)//10)%10)

r1= (10*a)+b
r2= (10*c)+d

print r1
print r2