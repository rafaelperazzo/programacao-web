# -*- coding: utf-8 -*-
from __future__ import division
a=float(input('Digite o valor do investimento:'))
t=float(input('Digie o valor da taxa de crescimento anual:'))
n=10
i=0
for i in range(0,n,0):
    a=a+(a*t)
    i=i+a
    print('%.2f'%i) 
    