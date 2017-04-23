# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
a=float(input('Digite o valor do investimento:'))
b=float(input('Digite o valor da taxa de cresimento:'))
c=0
while(c<=9):
    a=(a)+(a*b)
    c=c+1
    print('%.2f' %a)