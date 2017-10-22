# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
n = float(input('Digite o valor de n: '))
t = float(input('Digite o valor de t: '))

i=1
while(i<11):
    valor=n+(n*t)
    i=i+1
print('%.2f' %valor)
