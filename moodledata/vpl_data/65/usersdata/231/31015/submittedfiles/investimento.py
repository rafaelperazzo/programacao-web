# -*- coding: utf-8 -*-
from __future__ import division

inv=int(input('digite o valor do investimento :'))
taxa=float(input('digite valor da taxa :'))
t=taxa/100
a=inv+t*inv
print('lucros em 1 ano :%.2f'%a)
