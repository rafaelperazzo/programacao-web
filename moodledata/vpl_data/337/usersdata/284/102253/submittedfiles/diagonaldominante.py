# -*- coding: utf-8 -*-
n=(int(input('digite a ordem da matriz: ')))
while(True):
    if n<2:
        n=(int(input('digite a ordem da matriz: ')))
    else:
        break
matriz=[]
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite o elemento (%d,%d): ' %(i+1,j+1))))
    
soma_dp=0
for i in range(0,n,1):
    for j in range(0,n,1):
        if i==j:
            soma_dp=soma_dp+matriz[i][j]
cont=0
for i in range(0,n,1):
    if sum(matriz[i])>soma_dp:
        cont=cont+1
for j in range:
    soma_colunas=0
    for i in range(0,n,1):
        soma_colunas=matriz[i][j]+soma_colunas
    if soma_colunas>soma_dp:
        cont=cont+1
if cont>0:
    print('NAO')
else:
    print('SIM')
            
            
            
            
            
            
            
            
            
            
            
            
            
        
