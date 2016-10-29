# -*- coding: utf-8 -*-
from __future__ import division
soma=0
soma2=0
cont1=0
cont2=0
n=input('Digite o valor de n:')
a=0
while n>a:
    a=a+1
    p=input('Digite o um número da sequência:')
    if p%2!=0:
        soma=soma+p
        cont1=cont1+1
        print(soma)
    if p%2==0:
        soma2=soma2+p
        print(soma2)
        cont2=cont2+1
print(cont1)
print(cont2)