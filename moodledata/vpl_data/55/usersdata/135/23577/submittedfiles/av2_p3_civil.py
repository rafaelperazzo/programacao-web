# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def peso_peca(matrix,posicao_x,posicao_y):
    peso=0
    for i in range(0, matrix.shape[0],1):
        peso=peso+matrix[posicao_x,i]+matrix[i,posicao_y]
    peso=peso-2*(matrix[posicao_x,posicao_y])
    return int(peso)

n=input("Entre com o valor 'n' da dimensao da matriz: ")
matriz=np.zeros((n,n))
print
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        print"Elemento do indice %.f,%.f"%(i,j)
        matriz[i,j]=input("Entre com o valor: ")
    print
print "Sua matriz:"
print matriz

print
x=input("Entre com o indice 'x' da peca: ")
y=input("Entre com o indice 'y' da peca: ")

print "Peso da peca escolhida: ",peso_peca(matriz,x,y)


