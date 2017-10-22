# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento=float(input('Digite um valor para o investimento: '))
taxa=float(input('Digite um valor de taxa: '))
final = (investimento*((taxa**10)-1)/(taxa-1))
while investimento < final:
    investimento = investimento + taxa * investimento
    print ('%.2f' %investimento)