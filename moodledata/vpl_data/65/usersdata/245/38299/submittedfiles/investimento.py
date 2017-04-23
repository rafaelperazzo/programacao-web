# -*- coding: utf-8 -*-
from __future__ import division
a=float(input('Digite o valor do investimento:'))
t=float(input('Digie o valor da taxa de crescimento anual:'))
n=10
i=a
for i in range(1,n+1,1):
    s=a+(a*t)
    i=i+s
    print(i) 
    