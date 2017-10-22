# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
i=float(input('digite o valor do investimento: '))
a=float(input('digite o tempo de investimento em anos: '))
t=(i*0.045*a)
l=(i+t)
for a in range(1,10,1):
    print(l)
    
