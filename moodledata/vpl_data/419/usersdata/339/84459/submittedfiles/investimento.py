# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

i=float(input('digite o valor inicial do investimento: '))
t=float(input('digite a taxa de crescimento percentual: '))
cont=0
t=t/100


while cont<10:
    print('%.2f' %i)
    i=i+(t*i)
    cont+=1





