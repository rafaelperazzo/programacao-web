# -*- coding: utf-8 -*-

mat = []
n = int(input('Digite n: '))
m = int(input('Digite m: '))
for i in range(0,n,1):
    linha = []
    for j in range(0,m,1):
        linha.append(int(input('Digite m: ')))
    mat.append(linha)
for j in range(0,m,1):
        x = sum(mat[j])
print (x)
