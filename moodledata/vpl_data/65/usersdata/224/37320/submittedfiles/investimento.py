# -*- coding: utf-8 -*-
from __future__ import division

a=float(input('O investimento inicial é de: '))
t=float(input('A taxa de crescimento percentual é de: '))
investimento=a
i=1
for i in range(1,11,1):
    investimento=investimento+a*t*i
    print(investimento)