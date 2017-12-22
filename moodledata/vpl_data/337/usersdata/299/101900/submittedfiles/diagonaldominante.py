# -*- coding: utf-8 -*-
matriz=[]
n=int(input(''))
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    matriz.append(linha)
    
    
cont=0
for i in range(0,n,1):
    for j in range(0,n,1):
        x=sum(matriz[i][j])-matriz[i][i]
        if matriz[i][i]>x:
            cont+=0
        else:
            cont+=1
if cont!=0:
    print('SIM')
else:
    print('NÃO')
            
        