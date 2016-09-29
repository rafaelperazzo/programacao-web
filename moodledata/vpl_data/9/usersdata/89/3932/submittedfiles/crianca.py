# -*- coding: utf-8 -*-
from __future__ import division
#entrada
p1=input('digite o valor do peso no lado esquerdo p1:')
c1=input('digite o valor do comprimento da gangorra lado esquerdo c1:')
p2=input('digite o valor do peso no lado direto p2:')
c2=input('digite o valor do comprimento da gangorra lado direito c2:')
#processamento e saida
if p1*c2==p2*c2:
    print('0')
elif p1*c1<p2*c2:
    print('-1')
else:
    print('1')


