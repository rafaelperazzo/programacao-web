# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento=float(input('Digite um valor para o investimento: '))
taxa=float(input('Digite um valor de taxa: '))
q = investimento * taxa
final = investimento+(10)*q
while investimento < final:
    investimento = investimento + taxa * investimento
    print ('%.2f' %investimento)