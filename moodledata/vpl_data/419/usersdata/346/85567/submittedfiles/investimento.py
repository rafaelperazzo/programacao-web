# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

a=100.0
b=2500.50
investimento=0
for i in range (0,11,1):
    investimento = investimento+0.05*investimento
    print(investimento)