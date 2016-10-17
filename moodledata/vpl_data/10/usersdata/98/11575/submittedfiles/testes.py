# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
n=input('Digite o valor de n: ')
cont=0
soma=0
while True:
    a=n%10
    soma=soma+(a*(2**cont)
    n=n//10
    cont=cont+1
    if n==0:
        break