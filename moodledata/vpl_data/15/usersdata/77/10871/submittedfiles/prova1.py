# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
a=int(input('Digite o valor da primeira carta'))
b=int(input('Digite o valor da segunda carta'))
c=int(input('Digite o valor da terceira carta'))
d=int(input('Digite o valor da quarta carta'))
e=int(input('Digite o valor da quinta carta'))

while a>1 and a<13 and b>1 and b<13 and c>1 and c<13 and d>1 and d <13 and e>1 and e<13:
    if a>b>c>d>e:
        print('D')
    elif e>d>c>b>a:
        print('C')
    else:
        print('N')

