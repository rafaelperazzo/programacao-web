# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
valor = float(input('Digite o valor: '))
t = float(input('Digite o valor de t: '))

i=1
while(i<11):
    valor=valor+(valor*t)
    i=i+1
print('%.2f' %valor)
