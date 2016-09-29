# -*- coding: utf-8 -*-
from __future__ import division
import math

P = input('A posição da portinha P:')
R = input('A posição da portinha R:')

if P == 0:
    print('C')
elif P == 1 and R == 0:
    print('B')
else:
    print('A')