# -*- coding: utf-8 -*-
from __future__ import division

#Entradas e controle
investimento = float(input('Insira o valor do investimento: '))
taxa = float(input('Insira a taxa: '))
controle = 1

#Repetição
while controle<=10:
    investimento += investimento*taxa
    print('%.2f' % investimento)
    controle += 1