# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
Investimento=float(input('Digite um valor para o investimento: '))
taxa=float(input('Digite um valor de taxa: '))
n= (Investimento*(1-taxa**10)/1-taxa)
while True:
    investimento = Investimento + Investimento * taxa
    if (Investimento >= n):
        break
        print ('%.2f' % investimento)