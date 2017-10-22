# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento = float(input('Digite o valor do investimento inicial: '))
taxa = float(input('Digite a taxa de crescimento percentual: '))
n = 10
cont = 0
while cont < n:
    investimento = investimento + (investimento*taxa)
    cont = cont + 1
    print(investimento)
    investimento = investimento
    