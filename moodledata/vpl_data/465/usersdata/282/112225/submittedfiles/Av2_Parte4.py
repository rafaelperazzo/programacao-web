# -*- coding: utf-8 -*-
m=[]
n=int(input('Digite a dimensao da matriz: '))
while not n >=2:
    n=int(input('Digite a dimensao da matriz: '))
for i in range(0,n):
    linha=[]
    for j in range(0,n):
        linha.append(int(input('Digite os termos da matriz: ')))
    m.append(linha)
print(m)