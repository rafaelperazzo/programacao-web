# -*- coding: utf-8 -*-
from __future__ import division
valor=float(input('Digite o valor de investimento inicial :'))
taxa=float(input('taxa de crescimento percentual :'))
ano = 1
investimento = valor
while ano <= 10:
    investimento = investimento + (investimento * taxa)
    print ('saldo do ano %d e de R$%5.2f' % (ano, investimento))
    ano=ano+1

