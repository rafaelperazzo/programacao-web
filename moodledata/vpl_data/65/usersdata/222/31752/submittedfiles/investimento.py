# -*- coding: utf-8 -*-
from __future__ import division
valor=float(input('Digite o valor de investimento inicial :'))
taxa=float(input('taxa de crescimento percentual :'))
ano = 1
saldo = valor
while ano <= 10:
    saldo = saldo + (saldo * taxa)
    print ('saldo do ano %d e de R$%5.2f.' % (ano,saldo))
    ano=ano+1

