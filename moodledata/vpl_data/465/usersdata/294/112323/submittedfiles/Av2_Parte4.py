# -*- coding: utf-8 -*-
n= int(input('Digite a ordem da matriz nXn: '))
m=[]
for i in range (0,n,1):
    linha=[]
    for j in range (0,n,1):
        linha.append(int(input('Digite o elemento %d: ' %(i+1))))
    m.append(linha)
