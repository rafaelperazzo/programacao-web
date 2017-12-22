# -*- coding: utf-8 -*-

mat = []
n = int(input('Digite n: '))
m = int(input('Digite m: '))
for i in range(0,n,1):
    linha = []
    for j in range(0,m,1):
        linha.append(int(input('Digite m: ')))
    mat.append(linha)
for i in range(0,n,1):
    for j in range(0,m,1):
        x = sum(mat[j])
        if sum(mat[j]) < sum(mat[j+1]):
            print(sum(mat[j]))
