# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
n=float(input('digite o valor:'))
t=float(input('taxa:'))
i=0
c=n
while i<=11:
    c=c+(c*t)
    i=i+1
    print('%.2f'%c)    
    
