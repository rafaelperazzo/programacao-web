# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
v = float(input("digite o valor do investimento inicial= "))
i = float(input("digite o valor da taxa em decimal, ex:3% = 0.03 = "))
ano = 1
total = v
while ano<=10:
    total = total+(total*i)
    print ('%.2f' % total)
    ano = ano+1

    

