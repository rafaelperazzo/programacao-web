# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
capital = float(input('Digite o investimento inicial: '))
taxa = float(input('Digite a a taxa (Ex.: 1%=0.01): '))

i=1
while i<=10:
    juros = capital*taxa
    capital = capital + juros
    i=i+1
    print(capital)