# -*- coding: utf-8 -*-
from __future__ import division

n = input ('Digite um número:')
a = n
contador = 0
numero = 0
while a>=1:
    contador = contador +1
    a = a//10
i = 0
while i<contador:
    c = n%2
    numero = numero +(c*(10**i))
    n = n//2
print (numero)