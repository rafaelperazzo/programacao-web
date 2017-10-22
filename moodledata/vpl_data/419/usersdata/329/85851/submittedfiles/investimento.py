# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
v = float(input("digite o valor do investimento inicial= "))
i = float(input("digite o laor da taxa= "))
ano = 1
total = 0
while ano<=10:
    rendimento = v*(i/100)
    total += total+rendimento
    print ('%.2s' % total)
    ano = ano+1
    
    
     
    

