# -*- coding: utf-8 -*-
from __future__ import division

b =int(input('Digite um número inteiro na base binária:'))
d = b
cont = 0
while d>= 1:
    cont = cont +1
    d = d/10
    
soma = 0
for i in range(0, cont, 1):
    soma = soma + ((b%10)*(2**i))
    b = b//10
print(soma)


