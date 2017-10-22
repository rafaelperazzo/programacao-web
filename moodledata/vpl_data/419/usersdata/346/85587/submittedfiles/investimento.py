# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

investimentoA= float(input('Digite o valor para o investimento: '))
investimentoB= float(input('Digite outro valor para o investimento: '))
 
for i in range (1,11,1):
    
    investimentoA = investimentoA+0.0445*investimentoA
    print('%.2f' % investimentoA)
