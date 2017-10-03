# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

investimento= float(input('Digite o valor do investimento inicial:'))
taxa= float(input('Digite o valor da taxa anual:'))

investimento= investimento+(taxa*investimento)

print(investimento)