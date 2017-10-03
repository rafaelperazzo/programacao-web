# -*- coding: utf-8 -*-
from __future__ import division

#COMECE A PARTIR DAQUI!
import math
a = int(input('Digite a: '))
b = int(input('Digite b: '))
c = int(input('Digite c: '))
d = (-b)**2 - (4*a*c)
print('mostre o valor de {}'.format (d))
SRR = d ** 0,5
print('escreva o valor de {}'.format (SRR))
x1 = -(b+SRR)/2
print('mostre o valor de {}'.format(x1))
X2 = -(b-SRR)/2
print('mostre o valor de{}'.format (x2))
if d>='0':
    print('mostre {} e {}'.format(x1, x2))
else:
    print('SRR')
print('---FIM---')

