# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
a=float(input('digite a:'))
b=float(input('digite b:'))
n=10
for i in range(1,n+1,1):
    a1=a+(a*b)
    i=i+a1
    print('%.2f'%i)
