# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
x=input('Digite o valor do primeiro peso:')
y=input('Digite o valor do comprimento até o primeiro assento:')
z=input('Digite o valor do segundo peso:')
w=input('Digite o valor do comprimento até o segundo assento:')
#PROCESSAMENTO
a=(x*y)
b=(z*w)
#SAÍDA
if a>b:
    print('-1')
elif a<b:
    print('1')
else:
    print('0')
