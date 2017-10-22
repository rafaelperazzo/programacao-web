# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento = float(input('Digite o valor de investimento inicial: '))
taxa = float(input('Taxa de crescimento percentual: '))
while (investimento<2000) :
    print('%.2f' %investimento)
    investimento = investimento + taxa*investimento