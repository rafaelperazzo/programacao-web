# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
Investimento=float(input('Digite um valor para o investimento: '))
taxa=float(input('Digite um valor de taxa: '))
while Investimento < Investimento*((taxa**10)-1)/1-taxa:
    investimento = investimento + taxa * investimento
    print ('%.2f' %investimento)