# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
c=float(input('Digite o valor do investimento:'))
d=float(input('Digite o valor da taxa de cresimento percentual:'))
a=0
while(a<=9):
    c=(c)+(c*d)
    a=a+1
    print('%.2f' %c)