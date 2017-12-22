# -*- coding: utf-8 -*-
def eoq(matriz):
    coluna = len(mat[0])
    for j in range(coluna):
        x = sum(mat[j])
    return(x)

mat = []
n = int(input('Digite n: '))
m = int(input('Digite m: '))
for i in range(0,n,1):
    linha = []
    for j in range(0,m,1):
        linha.append(int(input('Digite m: ')))
    mat.append(linha)
print (eoq(mat))
