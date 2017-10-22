# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
i=float(input('digite o valor do investimento: '))
a=1
l=1000
while(0<a and a<=10):
    l=(i+i*0.045*a)
    print('%.2f' %l)
    l=(l+i*0.045*a)
    a=a+1
    
    
