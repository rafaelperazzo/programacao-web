# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
n=input("Digite o valor de n: ")
i=0
soma=0
while n>0:
    x=n%10
    soma=soma+(x*(2**i))
    i=i+1
print soma