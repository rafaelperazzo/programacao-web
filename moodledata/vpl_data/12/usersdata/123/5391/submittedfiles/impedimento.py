# -*- coding: utf-8 -*-
from __future__ import division
import math
L= int(input('Insira o valor de L:'))
R= int(input('Insira o valor de R:'))
D= int(input('Insira o valor de D:'))

if R>50 and L<R and R>D:
    print('S')
else:
    print('N')