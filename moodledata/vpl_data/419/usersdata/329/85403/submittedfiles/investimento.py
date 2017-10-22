# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
v = float(input("digite o valor do investimento inicial="))
i = float(input("digite o laor da taxa= "))
ano = 1
saldo = v
soma = 0
while ano <= 10:
    rendimento = (i/100)*v
    saldo = rendimento+saldo
    print ('%.2f' % saldo)
    ano = ano+1
    
    
     
    

