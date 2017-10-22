# -*- coding: utf-8 -*-
from __future__ import division

investimento = float(input('Digite o valor do investimento:'))
taxa = float(input('Digite o valor da taxa: '))

i = 0
i += 1

while ( i <= 10) :
    investimento = investimento + taxa * investimento
    print(i)
    print('{}' .format(investimento))