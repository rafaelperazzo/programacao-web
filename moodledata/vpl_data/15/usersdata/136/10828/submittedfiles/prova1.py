# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA

a = int(input('Digite o primeiro valor:'))
b = int(input('Digite o segundo valor:'))
c = int(input('Digite o terceiro valor:'))
d = int(input('Digite o quarto valor:'))
e = int(input('Digite o quinto valor:'))

if a<b<c<d<e:
    print('C')
    if a>b>c>d>e:
    print('D')
else: 
    print ('N')