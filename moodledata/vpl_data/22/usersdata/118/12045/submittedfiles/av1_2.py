# -*- coding: utf-8 -*-
from __future__ import division
import math

n1 = int(input('Digite o valor da primeira cor observada:'))
n2 = int(input('Digite o valor da segunda cor observada:'))
n3 = int(input('Digite o valor da terceira cor observada:'))
n4 = int(input('Digite o valor da quarta cor observada:'))

if n1 == n3 and n2 != n1 and n2 != n3 and n2 != n4 and n4 != n1 and n4 != n3:
    print('V')
elif n2 == n4 and n1 != n2 and n1 != n3 and n1 != n4 and n3 != n2 and n3 != n4:
    print('V')
else:
    print('F')
