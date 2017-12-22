# -*- coding: utf-8 -*-
def eoq(matriz):
    linha = len(mat)
    coluna = len(mat[0])
    for i in rage(linha):   
        for j in range(coluna):
            x = sum(coluna)
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

2 <= m <= 1000
0 <= i <= m-1
2 <= n <= 1000
0 <= j <= n-1
1 <= mat[i] <= 100