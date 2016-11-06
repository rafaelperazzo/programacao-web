# -*- coding: utf-8 -*-
from __future__ import division

n = input ('Digite um número:')
a = n
contador = 0
numero = 0
i = 0
while a//2>0:
    contador = contador +1
    a = a//2
while i<=contador:
    c = n%2
    numero = numero + (c*(10**i))
    n = n//2
    i = i+1
print (numero)