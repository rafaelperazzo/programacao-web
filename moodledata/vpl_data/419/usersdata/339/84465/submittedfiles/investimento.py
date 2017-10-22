# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

i=float(input('digite o valor inicial do investimento: '))
t=float(input('digite a taxa de crescimento percentual: '))
cont=0

while t<0 or t>1:
    t=float(input('digite a taxa de crescimento percentual: '))

while cont<10:
    i=i+(t*i)
    print('%.2f' %i)
    cont+=1





