# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
v = float(input("digite o valor do investimento inicial="))
i = float(input("digite o laor da taxa= "))
ano = 1
saldo = v
saldo = v*(i/100)+v
while ano <= 10:
        print ('%.2f' % saldo)
        ano = ano + 1
print ('%.2f' % (saldo+v))
    
     
    

