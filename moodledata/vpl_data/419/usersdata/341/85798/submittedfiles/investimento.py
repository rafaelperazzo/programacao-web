# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento = float(input('Digite o valor do investimento inicial: '))
taxa = float(input('Digite a taxa de crescimento percentual: '))
n = 1
while n<11:
    valortotal = investimento*((1+taxa)**n)
    print ("%.2f" %valortotal)
    n = n + 1
    