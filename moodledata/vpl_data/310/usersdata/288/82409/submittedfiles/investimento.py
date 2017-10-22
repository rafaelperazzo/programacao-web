# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
Investimento=float(input('Digite um valor para o investimento: '))
taxa=float(input('Digite um valor de taxa: '))
while (Investimento < Investimento*(1-taxa**10)/1-taxa):
    investimento = Investimento + Investimento * taxa
    print ('%.2f' % investimento)