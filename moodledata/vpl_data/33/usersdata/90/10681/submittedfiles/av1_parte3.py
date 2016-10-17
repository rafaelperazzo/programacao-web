# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

n=input('Digite o valor de n:')
termo=1
denominador=1
soma=0

while termo<=n:
    if termo%2==1:
        soma=soma+1/denominador
    else:
        soma=soma-1/denominador
    termo=termo+1
    denominador==denominador+2

