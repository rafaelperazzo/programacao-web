# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
i=float(input('digite o valor do investimento: '))
a=1
for a in range(1,10,1):
    i=(1000+i*0.045*a)
    l=(1000+i*0.045*a)
    print('%.2f' %l)
    a=a+1
    
        
    
    
    
