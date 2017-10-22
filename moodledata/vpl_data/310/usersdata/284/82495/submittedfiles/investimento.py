# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
i=float(input('digite o valor do investimento: '))
a=int(input('digite o tempo de investimento em anos: '))
t=(i+i*0.045*a)
for a in range(0,10,1):
    print(t)
    t=t+t
