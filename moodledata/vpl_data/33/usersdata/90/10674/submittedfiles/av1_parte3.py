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
    denominador=demoninador+2
    
    print ('O valor de pi é %6.f%)
