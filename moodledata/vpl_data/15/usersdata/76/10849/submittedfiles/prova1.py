# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA


a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:')) 
c = int(input('Digite o valor de c:'))
d = int(input('Digite o valor de d:'))
e = int(input('Digite o valor de e:'))

if a>b>c>d>e:
    print('D')
    if a<b<c<d<e:
        print('C')
else:
    print('N')