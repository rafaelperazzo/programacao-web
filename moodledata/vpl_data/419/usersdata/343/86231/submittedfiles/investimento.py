# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento = float(input('Digite o valor de investimento inicial: '))
taxa = float(input('Taxa de crescimento percentual: '))
investimento = investimento + taxa*investimento
print('%.2f' %investimento)