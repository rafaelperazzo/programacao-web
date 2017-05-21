# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Informe o valor a: '))
b=int(input('Informe o valor b: '))
c=int(input('Informe o valor c: '))

for i in range (0,c+1,1):
    if (c%a)==0:
        print(c//a)
    else:
        x=c//a
        y=c%a
        if ()