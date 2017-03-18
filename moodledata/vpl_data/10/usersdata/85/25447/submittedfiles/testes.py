# -*- coding: utf-8 -*-
from __future__ import division

n= input('Digite o valor de n: ')

vc=0
cont1=0
max=0
for i in range(1,n+1,1):
    a= input('Digite o valor de a: ')
    if vc==a:
        cont1=cont1+1
        if cont1>max:
            max= cont1
    elif vc!=a:
        vc=a

print max