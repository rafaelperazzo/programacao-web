# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
i=float(input('digite o valor do investimento: '))
a=1
for a in range(1,10,1):
    i=(i+i*0.045*a)
    l=(i+i*0.045*a)
    print('%.2f' %l)
    l=(i+i*0.045*a)
    a=a+1
    
        
    
    
    
