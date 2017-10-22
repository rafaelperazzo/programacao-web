# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
InvestimentoInicial=float(input('Digite um valor para o investimento: '))
taxa=float(input('Digite um valor de taxa: '))
while (InvestimentoInicial < 2000):
    investimento = InvestimentoInicial + InvestimentoInicial * taxa
    print ('%.2f' % investimento)