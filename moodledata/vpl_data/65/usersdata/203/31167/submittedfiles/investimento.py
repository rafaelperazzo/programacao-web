# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento=float(input('Investimento inicial: '))
taxa=float(input('Taxa de crescimento decimal: '))
for i in range (1,11,1):
    ganhos=investimento+investimento*taxa
    print(ganhos)