# -*- coding: utf-8 -*-
from __future__ import division

#COMECE A PARTIR DAQUI!
import math
a = int(input('Digite a: '))
b = int(input('Digite b: '))
c = int(input('Digite c: '))
d = (-b)**2 - (4*a*c)
print('o delta é {}'.format(d))
raiz  = math.sqrt(d)
print(' a raiz de delta é {}'.format(raiz))