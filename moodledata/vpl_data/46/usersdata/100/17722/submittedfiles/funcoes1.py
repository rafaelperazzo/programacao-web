# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    #escreva o código da função crescente aqui
    for i in range (0,len(lista),1):
        if lista(i) > lista (i-1):
            print 'crescente'
        elif lista(i) < lista (i-1):
            print 'decrescente'
    return crescente
#escreva as demais funções





#escreva o programa principal
n =  input('tamanho:')
lista = []
for i in range (0,n,1):
    lista.append(input('elementos:'))
    
    