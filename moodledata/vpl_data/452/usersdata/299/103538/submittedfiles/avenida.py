# -*- coding: utf-8 -*-
m=int(input(''))
n=int(input(''))
bairro=[]
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    bairro.append(linha)
#analise das colunas dos bairros
colunas=[]
for i in range(0,n,1):
    soma=0
    for j in range(0,m,1):
        soma+=bairro[j][i]
    colunas.append(soma)

resultado=sorted(colunas)

print(resultado[0])

