# -*- coding: utf-8 -*-
from __future__ import division
investimento=float(input('Digite o valor de investimento inicial :'))
taxa=float(input('taxa de crescimento percentual :'))
for i in range (1, 10, 1):
    investimento = investimento + (investimento * taxa)
    print (' %d R$%.2f' % (ano, investimento))
    

