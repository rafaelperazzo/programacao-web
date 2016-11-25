# -*- coding: utf-8 -*-
from __future__ import division

'''
EXERCÍCIO 42
Recorte retangular

0 0 0 0 0 
0 1 0 0 0
1 0 0 0 1
0 0 0 0 0
0 0 0 0 0

O que temos que encontrar ou procurar ?
-> Coluna da esquerda
-> Coluna da direita
-> Linha de cima
-> Linha de baixo

1) PASSO 1: Encontrar a coluna da esquerda

'''

def colunaEsquerda(a):
    col = a.shape[1]-1
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                if j < col:
                    col = j
    return col

    
    
    
    
    
