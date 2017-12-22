# -*- coding: utf-8 -*-
a=[]
n = int(input('Digite a quantidade de elementos de a: '))
m = int(input('Digite a quantidade de elementos de a: '))
for i in range(0,n,1):
    linha=[]
    for j in range(0,m,1):
        linha.append(int(input('Digite o termo: ')))
    a.append(linha)
print(a)
    
    