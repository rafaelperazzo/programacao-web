# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont = 0
    for i in range(0,len(lista),1):
        if lista[i] >= lista[i+1]:
            cont = cont +1
    if cont == 0:
        return 'S'
    else:
        return 'N'

def decrescente(lista):
    cont = 0
    for i in range(0,len(lista),1):
        if lista[i] <= lista[i+1]:
            cont = cont +1
    if cont == 0:
        return 'S'
    else:
        return 'N'

def consecutivos(lista):
    cont = 0
    for i in range(0,len(lista),1):
        if lista[i] == lista[i+1]:
            cont = cont +1
    if cont != 0:
        return 'S'
    else:
        return 'N'
        









#escreva o programa principal
