# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    posicaomax=0
    for i in range (1,len(lista)-1,1):
        if (l[i]>l[i-1]):
            posicaomax = i
    
    


n = input('Digite a quantidade de elementos da lista: ')
l = []

for i in range (0,n,1):
    l.append ( input ('Digite um elemento:'))


