# -*- coding: utf-8 -*-
n=int(input('Determine a dimensão da matriz quadrada A: '))
A=[]
for i in range(n):
    linha=[]
    for j in range(n):
        linha.append(int(input('Digite o elemento %d x %d da matriz A: '%(i,j))))
    A.append(linha)
c=int(input('Digite a quantidade de cidades do intinerário: '))
for i in range(c):
    c.append(int(input('Digite os números correspondentes as cidades do intinerário: ')))
valor=0
for i in range(1,c,1):
    valor+=A[c[i-1]][c[i]]
    