# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))

cont=0
quantidadea=c//a
quantidadeb=0

while quantidadea>=0:
    troco=c-quantidadea*a
    if troco%b==0:
        quantidadeb=troco//b
        cont=cont+1
        break
    else:
        quantidadea=quantidadeb-1
        if cont>0:
            print(quantidadea)
            print(quantidadeb)
        else:
            print('n')
