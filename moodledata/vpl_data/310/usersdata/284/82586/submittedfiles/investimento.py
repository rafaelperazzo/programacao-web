# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
a=float(input('digite o investimento inicial: '))
b=float(input('digite o percentual: '))
i=1
s=a
while (0<i<=10):
    s=s+(s*b)
    i=i=1
    print('%.2f' %s)
    
