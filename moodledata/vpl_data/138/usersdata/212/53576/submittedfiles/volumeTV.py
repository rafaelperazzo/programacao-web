# -*- coding: utf-8 -*-
v=int(input('digite o valor do volume inicial:'))
t=int(input('digite o número de vezes que o volume foi modificado:'))
i=1
while i<=t:
    a=int(input('digite o valor do volume a ser incrementado:'))
    v=v+a
    print(v)
    i=i+1
print(v)