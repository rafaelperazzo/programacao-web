# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
i=float(input('digite o valor do investimento: '))
t=float(input('digite a taxa de crescimento percentual: '))

cont=1
while(cont<=10):
    i=i+i*t
    cont=cont+1
    print('%.2f' %i)




