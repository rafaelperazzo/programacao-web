# -*- coding: utf-8 -*-
from __future__ import division
import math

n1 = int(input('Digite o valor da primeira cor observada:'))
n2 = int(input('Digite o valor da segunda cor observada:'))
n3 = int(input('Digite o valor da terceira cor observada:'))
n4 = int(input('Digite o valor da quarta cor observada:'))

if n1 == n3 and n2 != n4:
    print('V')
if n2 == n4 and n1 != n3:
    print('V')
if n1 == n4 and n2 != n3:
    print('F')
