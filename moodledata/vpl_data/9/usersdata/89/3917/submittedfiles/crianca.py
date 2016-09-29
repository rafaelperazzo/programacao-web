# -*- coding: utf-8 -*-
from __future__ import division
#entrada
p1=input('digite o valor do peso no lado esquerdo:')
c1=input('digite o valor do comprimento da gangorra lado esquerdo')
p2=input('digite o valor do peso no lado direto:')
c2=input('digite o valor do comprimento da gangorra lado direito')
#processamento e saida
if p1*c1==p2*c2:
    print('0')
elif p1*c1<p2*c2:
    print('-1')
else:
    print('1')


