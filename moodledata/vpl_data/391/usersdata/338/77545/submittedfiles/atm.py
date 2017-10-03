# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
x = (int(input('digite o valor a ser sacado: ')))
n20 = x//20
if n20 > 0:
    n10 = (x%20)//10
else:
    n10 = x//10

if n10 > 0:
    n5 = (x%10)//5
else:
    n5 = x//5
    


print(n20)
print(n10)
print(n5)




"""
n10 = resto1//10
a = (x - (n10)*10)




if resto1 > 0:
    n5 = a//5
    a = (x - (n5)*5)
else:
    n5 = a//5
    
    
    
n2 = a//2
a = (x - (n2)*2)

n1 = a//1


print(n20)
print(n10)
print(n5)
print(n2)
print(n1)
"""