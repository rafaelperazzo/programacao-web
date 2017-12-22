# -*- coding: utf-8 -*-
n=int(input('digite a dimensao da matriz: '))
m=[]
for i in range(0,n,1):
    colunas=[]
    for j in range(0,n,1):
        colunas.append(float(input('digite um termo da matriz: ')))
    m.append(colunas)
print(m)
