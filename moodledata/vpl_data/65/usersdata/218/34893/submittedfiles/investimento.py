# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
v=float(input('digite o valor do investimento:'))
t=float(input('digite o valor da taxa e crescimento anual:'))
i=1
for i in (1,11,1):
    valor=v*(1+(i*t))
    print(valor)