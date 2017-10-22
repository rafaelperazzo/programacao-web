# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
a = int(input('Digite o valor inicial: '))
b = float(input('Digite o valor do juros anual: '))
for i in range(a,a+10,1):
    a = a + a*b
    print ('%.2f' %a)
