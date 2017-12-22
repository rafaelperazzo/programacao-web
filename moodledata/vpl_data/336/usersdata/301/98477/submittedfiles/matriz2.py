# -*- coding: utf-8 -*-
n= int(input('Digite o número de linhas: '))
lista=[n,n]
for i in range (0,n,1):
    for j in range (0,n,1):
        lista[i][j]= int(input('Digite o elemento da linha%d da coluna%d: ' %((j+1),(i+1))))

