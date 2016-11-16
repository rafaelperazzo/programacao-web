# -*- coding: utf-8 -*-
from __future__ import division

def quantidade (lista1, lista2):
    contador = 0
    for i in range (0,len(lista2),1):
        if lista2[i] in lista1:
            contador = contador +1
    return contador
    
n = input ('Digite a quantidade de termos de a:')
