# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o valor de n: ')
a = []

for i in range(0,n,1):
    a.append(input('Digite um elemento: '))
    
Ma = (a[0] + a[1] + a[2] + a[3] + a[4])/n

print(a[0])
print(a[n-1])
print(Ma)