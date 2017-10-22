# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento = float(input('Digite o valor do investimento: '))
taxa = float(input('Digite o valor da taxa: '))
a=1
while (a<11):
    total = investimento*((1+taxa)**a)
    print('%.2f' %total)
    a+=1