 # -*- coding: utf-8 -*-
from __future__ import division
investimento=float(input('Digite o Valor do Investimento Inicial:'))
t=float(input('Digite a Taxa de Juros Anual:'))
if (t<=1):
    investimento=investimento*t*investimento
    print('%2.f' %investimento)