# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
mt=[]
m = int(input('insira a linha: '))
n = int(input('insira a coluna: '))
for i in range(0,m):
    linha=[]
    for j in range(0,n):
        linha.append(int(input('insira os termos da matriz: ')))
    mt.append(linha)
print(mt)

b=[]
for i in range(0,mt.shape[0],1):
    soma = 0
    for j in range(0,mt.shape[1],1):
        soma = soma + mt[i][j]
    b.append(soma)
print(b)        