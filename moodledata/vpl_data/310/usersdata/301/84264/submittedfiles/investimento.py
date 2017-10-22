# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento= float(input('digite o valor investido: '))
taxa= float(input('digite o valor da taxa de crescimento percentual:[0,1] '))
t=1
for t in range(1,11,1):
    investimento=investimento+ (taxa*investimento)
    print('%.2f' %(investimento))

