# -*- coding: utf-8 -*-
from __future__ import division
a=input(' digite o valor do peso do lado esquerdo:')
b=input(' digite o valor do comprimento da gangorra do lado esquerdo:')
c=input(' digite o valor do peso do lado direito:')
d=input(' digite o valor do comprimento da gangorra do lado direito:')
if a*b==c*d:
    print('0')
if a*b>c*d:
    print('-1')
if a*b<c*d:
    print('1')
