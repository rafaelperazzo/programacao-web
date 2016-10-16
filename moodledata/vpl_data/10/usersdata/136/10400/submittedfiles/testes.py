# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
n = int(input('digite n:'))
i = 1
soma = 0
while i<=n:
    if i%2==0:
        soma = soma - i/(i**2)
    else:
        soma = soma + i/(i**2)
    i = i + 1
print (soma)
