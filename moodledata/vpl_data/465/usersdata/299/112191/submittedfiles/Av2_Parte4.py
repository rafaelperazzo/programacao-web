# -*- coding: utf-8 -*-
n=int(input('Determine a dimensão da matriz quadrada A: '))
A=[]
for i in range(n):
    linha=[]
    for j in range(n):
        linha.append(int(input('Digite o elemento %d x %d da matriz A: '%(j,i))))
    A.append(linha)
        