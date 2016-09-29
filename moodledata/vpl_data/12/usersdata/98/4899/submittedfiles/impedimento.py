# -*- coding: utf-8 -*-
from __future__ import division
import math
#COMECE SEU CÓDIGO AQUI
L=int(input('Digite o valor de L: '))
R=int(input('Digite o valor de R: '))
D=int(input('Digite o valor de D: '))

if R>50 and L<R and R<D:
    print('N')
else:
    print('S')