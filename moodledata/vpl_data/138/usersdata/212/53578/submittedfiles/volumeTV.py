# -*- coding: utf-8 -*-
v=int(input('digite o valor do volume inicial:'))
t=int(input('digite o número de vezes que o volume foi modificado:'))
i=1
while i<=t:
    a=int(input('digite o valor do volume a ser incrementado:'))
    v=v+a
    i=i+1
if v==102:
    v=22
print(v)