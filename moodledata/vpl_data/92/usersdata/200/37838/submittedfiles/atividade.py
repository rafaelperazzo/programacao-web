# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de n:'))
if n<0:
    n*(-1)
contagem=1
soma=0
while contagem<=n:
    soma=soma+(contagem/denominador)
    contagem=contagem+1
    denominador=n-1
print('%.5f' %soma)
