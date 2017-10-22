# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento=float(input('Digite um valor para o investimento: '))
taxa=float(input('Digite um valor de taxa: '))
while (investimento < (investimento*(1-(taxa^10)/1-taxa))):
    investimento=investimento+investimento*taxa
    print (investimento)