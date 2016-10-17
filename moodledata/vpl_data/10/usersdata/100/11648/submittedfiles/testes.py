# -*- coding: utf-8 -*-
from __future__ import division
#COMECE AQUI ABAIXO
n = input ('Digite o valor decimal:')
cont=0
soma=0
while True:
    a=n%10
    soma=soma+(n%2)*10**cont
    n=n//2
    cont=cont +1
    if n==0:
        break
print soma