# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
v = float(input("digite o valor do investimento inicial= "))
i = float(input("digite o laor da taxa= "))/100
ano = 10
total = v
rendimento = 0
while v>=0:
    rendimento = v*i
    total = total+rendimento
    print ('%.2f' % total)
    ano = ano+1
    
    
     
    

