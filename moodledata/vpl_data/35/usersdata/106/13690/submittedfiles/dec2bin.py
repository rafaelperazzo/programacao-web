# -*- coding: utf-8 -*-
from __future__ import division

p = input ('Digite um número:')
q = input ('Digite um número:')
menor = p
maior = q
contador1 = 0
contador2 = 0
while menor>=1:
    contador1 = contador1 + 1
    menor = menor//10
print (contador1)