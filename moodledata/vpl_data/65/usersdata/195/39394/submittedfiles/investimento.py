# -*- coding: utf-8 -*-
from __future__ import division
investimento=float(input('digite o valor do investimento inicial :'))
taxa=float(input('taxa de crescimento percentual :'))
for i in range (1, 11, 1):
    investimento= investimento + (investimento * taxa)
    print ('R$%.2f' % investimento)