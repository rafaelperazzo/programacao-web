# -*- coding: utf-8 -*-
from __future__ import division
import math
#entrada
L = int(input('digite o valor em metros do lançador:'))
R = int(input('digite o valor em metros do receptor:'))
D = int(input('digite o valor em metros do defensor:'))
#processamento e saida
if R>50 and L<R and R>D:
    print('S')
else:
    print('N')