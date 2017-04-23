# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
inv_ini = float(input("Qual o valor do seu investimento inicial? "))
tax_cre = float(input("Qual a taxa de de crescimento anual(Ex.: Ex: 5% deve ser escrito como 0.05.)? "))

for i in range(10):
    inv_ini = inv_ini+tax_cre*inv_ini
    print (inv_ini)
