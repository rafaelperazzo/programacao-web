# -*- coding: utf-8 -*-
from __future__ import division


def contido (x,y):
    cont = 0
    for i in range(0,len(y),1):
        #O QUE FAZER COM y[i]
        if y[i] in x:
            cont = cont + 1
    
    return cont


#PROGRAMA PRINCIPAL
n = input('Digite a quantidade de elementos de a: ')
m = input('Digite a quantidade de elementos de b: ')

a = []
for i in range(0,n,1):
    a.append(input('Digite um valor para a: '))

b = []
for i in range(0,m,1):
    b.append(input('Digite um valor para b: '))

#PROCESSAMENTO E SAÍDA
print contido(a,b)

print contido(a,b)
#Como fazer pra mostrar os elementos de a que estão em b ?
#print contido(b,a)



