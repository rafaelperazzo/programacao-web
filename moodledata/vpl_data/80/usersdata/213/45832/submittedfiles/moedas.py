# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Informe o valor a: '))
b=int(input('Informe o valor b: '))
c=int(input('Informe o valor c: '))

for i in range (0,a+1,1):
    if (a%b)==0:
        print(a//b)
    elif (a%c)==0:
        print(a//c)
    else:
        print('NAO')