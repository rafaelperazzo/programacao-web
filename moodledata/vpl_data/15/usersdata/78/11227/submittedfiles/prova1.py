# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
a=int(input('digite o valor de a (entre 1 e 13):'))
b=int(input('digite o valor de b (entre 1 e 13):'))
c=int(input('digite o valor de c (entre 1 e 13):'))
d=int(input('digite o valor de d (entre 1 e 13):'))
e=int(input('digite o valor de e (entre 1 e 13):'))

if a<b<c<d<e:
    print('C')
else:
    if a>b>c>d>e:
        print('D')
    else:
        print('N')



