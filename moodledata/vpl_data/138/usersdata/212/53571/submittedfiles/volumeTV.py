# -*- coding: utf-8 -*-
v=int(input('digite o valor do volume inicial:'))
t=int(input('digite o número de vezes que o volume foi modificado:'))
cont=1
while cont<=t:
    a=int(input('digite o valor do volume a ser incrementado:'))
    f=v+a
    cont=cont+1
print(f)