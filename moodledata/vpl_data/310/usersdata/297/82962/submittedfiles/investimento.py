# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento= float(input('digite o valor do seu investimento: '))
taxa= float(input('digite o valor da taxa de crecimento em numeros decimais: '))
anos=10
while anos<=10 :
    investimento=investimento+taxa*investimento
    print('%.2f' %investimento)