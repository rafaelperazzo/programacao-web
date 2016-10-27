# -*- coding: utf-8 -*-
from __future__ import division
import funcoes
m=input('Digite o numero m de termos da formula de pi:')
e=input('Digite o epsilon para o calculo da razao aurea:')
So=3
a=2
for i in range(1,m+1,1):
    if (a//2)%2==0:
        So=So-4/(a*(a+1)*(a+2))
    else:
        So=So+4/(a*(a+1)*(a+2))
    a=a+2
So=pi


