# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
valor = float(input('Insira o valor do investimento: '))
tx = float(input('Insira a taxa anual: '))
cont = 1
while cont <= 10:
    valor = valor+(valor*tx)
    print (valor)
    cont = cont+1


    