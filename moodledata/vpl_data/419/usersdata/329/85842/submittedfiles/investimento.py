# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
v = float(input("digite o valor do investimento inicial= "))
i = float(input("digite o laor da taxa= "))/100
ano = 1
total = v
rendimento = 0
while ano<=10:
    total += total(+v*i)
    print ('%.2f' % total)
    ano = ano+1
    
    
     
    

