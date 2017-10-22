# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
i=float(input('digite o valor do investimento: '))
a=1
while(0<a and a<=10):
    l=(1000+i*0.045*a)
    print(l)
    i=l
    a=a+1
    
    
