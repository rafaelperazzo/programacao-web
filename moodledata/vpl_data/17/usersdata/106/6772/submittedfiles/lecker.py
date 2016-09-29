# -*- coding: utf-8 -*-
from __future__ import division
import math
#entrada
a = input ('Digite um número:')
b = input ('Digite um número:')
c = input ('Digite um número:')
d = input ('Digite um número:')

# processamento
if a>b>c>d:
    print('S')
elif a<b>c>d:
    print ('S')
elif a<b<c>d:
    print ('S')
elif a<b<c<d:
    print ('S')
else:
    print ('N')