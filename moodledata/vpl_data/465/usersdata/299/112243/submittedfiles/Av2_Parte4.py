# -*- coding: utf-8 -*-
n=int(input('Determine a dimensão da matriz quadrada A: '))
A=[]
for i in range(n):
    linha=[]
    for j in range(n):
        linha.append(int(input('Digite o elemento %d x %d da matriz A: '%(i,j))))
    A.append(linha)
c=int(input('Digite a quantidade de cidades do intinerário: '))
cid=[]
for i in range(c):
    cid.append(int(input('Digite os números correspondentes as cidades do intinerário: ')))
valor=0
for i in range(1,c,1):
    valor+=A[cid[i-1]][cid[i]]
print(valor)
    