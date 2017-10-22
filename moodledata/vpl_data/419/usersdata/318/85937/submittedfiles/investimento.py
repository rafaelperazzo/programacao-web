# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

i = float(input('Digite o valor do investimento :'))
t = float(input('Digite a taxa de crescimento percentual (em %) :'))

t = t*(1/100)

investimento = i*t
print(investimento)