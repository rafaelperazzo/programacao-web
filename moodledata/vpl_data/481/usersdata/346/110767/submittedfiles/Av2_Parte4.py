# -*- coding: utf-8 -*-

n= int(input('Digite valor de n: '))

matriz=[]
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(input('Valores da matriz: '))
    matriz.append(linha)
    
