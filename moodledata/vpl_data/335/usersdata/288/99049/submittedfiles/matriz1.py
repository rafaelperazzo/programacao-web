# -*- coding: utf-8 -*-
matriz=[]
m=int(input('Digite a quantidade de linhas (m): '))
n=int(input('Digite a quantidade de colaunas (n): '))
for i in range (0,m,1):
    linha=[]
    for j in range (0,n,1):
        linha.append(int(input('Digite o%dª avalor para a linha: '%(j+1))))
    matriz.append(linha)
for i in range (0,m,1):
    print (matriz[i])
    
