# -*- coding: utf-8 -*-
m=int(input('Digite a quantidade de listas: '))
n=int(input('Digite a quantidade de elementos de cada lista: '))
for i in range (0,m,1):
    listai=[]
    for j in range (0,n,1):
        listai.append(int(input('Digite o elemento%.d da listai: ' %(i+1))))
for i in range (0,m,1):
    somai=0
    for j in range (0,n,1):
        somai+=listai[j]
    mediai=somai/(n-1)
    print(mediai)