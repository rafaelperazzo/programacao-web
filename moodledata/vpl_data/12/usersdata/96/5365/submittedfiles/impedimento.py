# -*- coding: utf-8 -*-
from __future__ import division
import math
L = input('Digite a posição do lançador:')
R = input('Digite a posição do receptor:')
D = input('Digite a posição do defensor:')

if R > 50 and L < R and R > D:
    print('S')
else:
    print('N')