# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
i= int(input('Digite o valor do investimento inicial: '))
t= float(input('Digite o valor da taxa de crescimento percetual [0,1]: '))
t=1
for t in range (0,11,1):
    investimento= investimento + (taxa*investimento)
    print ('%.2f' %(investimento))