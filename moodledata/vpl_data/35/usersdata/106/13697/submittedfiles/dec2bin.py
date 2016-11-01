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
while maior>=1:
    contador2 = contador2 + 1
    maior = maior//10
while true:
    if p%(10**(contador2-contador1))==p:
        print ('S')
        break
    else:
        p = p//10
        contador2 = contador2-1
    if q<p:
        print('N')
        break