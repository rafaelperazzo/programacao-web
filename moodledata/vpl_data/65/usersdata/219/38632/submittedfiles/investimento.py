# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
deposito=float(input('Digite o deposito:'))
taxa=float(input('Digite a taxa:'))
investimento=float(input('Digite o investimento:'))
mês=1
while mes <= 10:
    investimento=investimento+taxa*investimento
    print('%d/%d/%d/%d/%d/%d/%d/%d/%d/%d')