# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
a=int(input('Digite o valor da primeira carta'))
b=int(input('Digite o valor da segunda carta'))
c=int(input('Digite o valor da terceira carta'))
d=int(input('Digite o valor da quarta carta'))
e=int(input('Digite o valor da quinta carta'))


    if 1<=a>b>c>d>e<=13:
        print('D')
    elif 1<=e>d>c>b>a<=13:
        print('C')
    else:
        print('N')

