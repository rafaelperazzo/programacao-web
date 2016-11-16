# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite a quantidade de elementos de a: ')
m = input('Digite a quantidade de elementos de b: ')

a = []
for i in range(0,n,1):
    a.append(input('Digite um valor para a: '))

b = []
for i in range(0,m,1):
    b.append(input('Digite um valor para b: '))

cont = 0
for i in range(0,len(b),1):
    #O QUE FAZER COM CADA ELEMENTO DE B ? b[i]
    #Eu quero saber se b[i] está em a
    # if b[i] in a:
    if b[i] in a:
        cont = cont + 1

print cont
