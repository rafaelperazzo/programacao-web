# -*- coding: utf-8 -*-
from __future__ import division

n = int(input('digite n:'))
a=[]
for i in range(1,n+1,1):
    a.append(input('digite o item:'))
    soma=soma+a
media=soma/n
print('%.2f'%a[0])
print('%.2f'%a[n-1])
print('%.2f'%media)
print(a)
