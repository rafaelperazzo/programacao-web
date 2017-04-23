# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
n=float(input('digite o valor:'))
t=float(input('taxa:'))
i=1
contador=0
while i<=11:
    i=n+(n*t)
    contador=contador+1
    i=i+1
    print('%f'%i)    
    
