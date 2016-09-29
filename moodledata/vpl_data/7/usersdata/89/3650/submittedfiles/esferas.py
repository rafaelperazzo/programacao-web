# -*- coding: utf-8 -*-
from __future__ import division
#entrada
a=input('digite o valor de a :')
b=input('digite o valor de b :')
c=input('digite o valor de c :')
d=input('digite o valor de d :')
#processamento
if (a==b+c+d) and (b+c==d) and (b==c):
    print('S')
else :
    print('N')
