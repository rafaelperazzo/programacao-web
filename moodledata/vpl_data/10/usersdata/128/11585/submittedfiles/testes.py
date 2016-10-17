# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

n=input('Quantidade de números: ')
j=input('Insira um número: ')
m=input('Digite o módulo: ')
i=1
cont=0
while cont<=n:
    if i%m==j%m:
        print i
        cont=cont+1
    i=i+1