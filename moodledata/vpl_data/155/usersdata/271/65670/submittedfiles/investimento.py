# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
#ENTRADA
x = float(input('Digite o valor inicial de investimento: '))
y = float(input('Digite o valor da taxa anual: '))
#PROCESSAMENTO
a = x+(x*y)
b = a+(a*y)
c = b+(b*y)
print(a)
print(b)
print(c)
