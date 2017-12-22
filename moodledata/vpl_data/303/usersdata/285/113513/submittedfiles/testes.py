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